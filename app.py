"""
Bitki Hastalığı Tespiti - Flask Web Uygulaması
================================================
Çift Model Desteği: Tarla + Ev Bitkileri
"""

import os
import io
import json
import base64
import numpy as np
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image
from google import genai
from google.genai import types

# ─── Sabitler ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
IMG_SIZE = 224

# Model dosya yolları (öncelik sırasına göre)
PLANT_MODEL_PATHS = [
    BASE_DIR / "plant_model-2.onnx",              # Model 1 (ayrı eğitim - Düzeltilmiş)
    BASE_DIR / "plant_model.onnx",                # Model 1 (ayrı eğitim - Eski)
    BASE_DIR / "plant_disease_model_v3.onnx",      # v3 birleşik
    BASE_DIR / "plant_disease_model_v2.onnx",      # v2 birleşik
    BASE_DIR / "plant_disease_model.onnx",          # v1 orijinal
]
INDOOR_MODEL_PATH = BASE_DIR / "indoor_model-2.onnx"  # Model 2 (Düzeltilmiş)

PLANT_CLASS_NAMES_PATH = BASE_DIR / "plant_class_names.txt"
INDOOR_CLASS_NAMES_PATH = BASE_DIR / "indoor_class_names.txt"
CLASS_NAMES_PATH = BASE_DIR / "class_names.txt"  # Eski tek model uyumluluğu

# ─── Flask ─────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

# ─── Model Yöneticisi ──────────────────────────────────────────────────────
models = {}  # {"plant": {...}, "indoor": {...}}


def load_onnx_model(model_path, class_names_path, model_name):
    """Tek bir ONNX modelini yükle."""
    try:
        import onnxruntime as ort
        session = ort.InferenceSession(str(model_path))
        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name

        cls_names = []
        if class_names_path.exists():
            with open(class_names_path) as f:
                cls_names = [line.strip() for line in f if line.strip()]

        models[model_name] = {
            "session": session,
            "input_name": input_name,
            "output_name": output_name,
            "class_names": cls_names,
        }
        print(f"✓ {model_name.upper()} modeli yüklendi: {model_path.name} ({len(cls_names)} sınıf)")
        return True
    except Exception as e:
        print(f"⚠ {model_name} model hatası: {e}")
        return False


def load_models():
    """Tüm mevcut modelleri yükle."""
    # ── Plant model (tarla bitkileri)
    plant_loaded = False
    for path in PLANT_MODEL_PATHS:
        if path.exists():
            # Daima güncel plant_class_names.txt dosyasını kullan
            cn_path = PLANT_CLASS_NAMES_PATH
            if not cn_path.exists():
                cn_path = CLASS_NAMES_PATH # Fallback

            plant_loaded = load_onnx_model(path, cn_path, "plant")
            if plant_loaded:
                break

    if not plant_loaded:
        # Fallback: veri seti klasöründen sınıf isimleri
        train_dir = BASE_DIR / "New Plant Diseases Dataset(Augmented)" / \
                    "New Plant Diseases Dataset(Augmented)" / "train"
        if train_dir.exists():
            cls = sorted([d.name for d in train_dir.iterdir() if d.is_dir()])
            print(f"  Sınıf isimleri veri setinden alındı: {len(cls)}")

    # ── Indoor model (ev bitkileri)
    if INDOOR_MODEL_PATH.exists():
        load_onnx_model(INDOOR_MODEL_PATH, INDOOR_CLASS_NAMES_PATH, "indoor")

    # ── TensorFlow yedek (eski model)
    if not models:
        h5_path = BASE_DIR / "plant_disease_model.h5"
        if h5_path.exists():
            try:
                import tensorflow as tf
                model = tf.keras.models.load_model(str(h5_path))
                cls_names = []
                if CLASS_NAMES_PATH.exists():
                    with open(CLASS_NAMES_PATH) as f:
                        cls_names = [l.strip() for l in f if l.strip()]
                models["plant"] = {
                    "session": model,
                    "type": "tensorflow",
                    "class_names": cls_names,
                }
                print(f"✓ TensorFlow modeli yüklendi: {h5_path.name}")
            except Exception as e:
                print(f"⚠ TF hatası: {e}")

    if not models:
        print("⚠ Hiçbir model bulunamadı. Demo modunda çalışılıyor.")


# ─── Hastalık Bilgisi ───────────────────────────────────────────────────────
try:
    from disease_info import DISEASE_INFO, get_disease_info, get_severity_color
except ImportError:
    DISEASE_INFO = {}
    def get_disease_info(name): return {"name": name, "emoji": "🌿", "severity": "Bilinmiyor",
                                        "description": "", "symptoms": [], "treatment": []}
    def get_severity_color(s): return "#6b7280"


# ─── Görüntü İşleme ─────────────────────────────────────────────────────────
def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """EfficientNet uyumlu preprocessing: [0, 255] aralığında RGB RGB verir."""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)
    # NOT: Keras EfficientNet (B0-B7) Rescaling ve Normalizasyon katmanlarını 
    # modelin içine (built-in) dahil ettiği için, piksel değerleri 0-255 arasında kalmalıdır.
    return np.expand_dims(arr, axis=0)


def predict_with_model(model_info, img_array):
    """Tek bir model ile tahmin yap."""
    if model_info.get("type") == "tensorflow":
        preds = model_info["session"].predict(img_array, verbose=0)[0]
    else:
        session = model_info["session"]
        preds = session.run(
            [model_info["output_name"]],
            {model_info["input_name"]: img_array}
        )[0][0]
        
    # INDOOR PENALTY (Ev bitkileri çok dominant olduğu için kalkanı deliyor)
    is_indoor = "indoor" in model_info.get("class_names", [])[0].lower() or "aloe" in model_info.get("class_names", [])[0].lower()
    
    # Basitçe dosya yolundan da tanınabilir
    if "indoor" in str(model_info.get("session")).lower():
        preds = preds * 0.6
        
    return preds


def make_prediction(image_bytes: bytes):
    """Tüm modelleri çalıştır, en yüksek güveni döndür."""
    if not models:
        return None, None

    arr = preprocess_image(image_bytes)
    all_candidates = []

    for model_name, model_info in models.items():
        try:
            preds = predict_with_model(model_info, arr)
            class_names = model_info["class_names"]

            top5_idx = np.argsort(preds)[::-1][:5]
            for idx in top5_idx:
                cn = class_names[idx] if idx < len(class_names) else f"Sınıf_{idx}"
                info = get_disease_info(cn)
                all_candidates.append({
                    "class": cn,
                    "confidence": float(preds[idx]),
                    "confidence_pct": round(float(preds[idx]) * 100, 2),
                    "name": info["name"],
                    "emoji": info["emoji"],
                    "severity": info["severity"],
                    "severity_color": get_severity_color(info["severity"]),
                    "description": info["description"],
                    "symptoms": info["symptoms"],
                    "treatment": info["treatment"],
                    "model": model_name,
                })
                
            # DEBUG LOGLARI
            print(f"[{model_name.upper()}] TAHMİNLER --->")
            for idx in top5_idx[:3]:
                cn = class_names[idx] if idx < len(class_names) else f"Sınıf_{idx}"
                print(f"   -> {cn}: {float(preds[idx])*100:.2f}%")
                
        except Exception as e:
            print(f"⚠ {model_name} tahmin hatası: {e}")

    if not all_candidates:
        return None, None

    # En yüksek güvene göre sırala
    all_candidates.sort(key=lambda x: x["confidence"], reverse=True)
    
    top_result = all_candidates[0]
    top_1 = all_candidates[0]["confidence_pct"] if len(all_candidates) > 0 else 0
    top_2 = all_candidates[1]["confidence_pct"] if len(all_candidates) > 1 else 0
    top_3 = all_candidates[2]["confidence_pct"] if len(all_candidates) > 2 else 0
    
    # NOT-A-LEAF (OOD) KONTROLÜ
    # 1. Eğer en yüksek ihtimal bile %65'in altındaysa (düşük güven), bu kesinlikle yaprak değildir.
    # 2. Eğer model %65 ile %90 arası bir kararsızlıktaysa:
    #    - Bu bir yapraksa, en azından ilk 2-3 hastalığın toplamı çok yüksektir (>%90).
    #    - Bu bir insansa/eşyaysa, model hiçbirine benzetemediği için olasılıklar daha dağılır.
    is_not_leaf = False
    if top_1 < 65.0:
        is_not_leaf = True
    elif top_1 < 90.0 and (top_1 + top_2 + top_3) < 90.0:
        is_not_leaf = True
        
    if is_not_leaf:
        not_a_leaf_result = {
            "class": "Unknown_Object",
            "confidence": top_result["confidence"],
            "confidence_pct": top_result["confidence_pct"],
            "name": "Bilinmeyen Nesne / Kamerayı Odaklayın",
            "emoji": "❓",
            "severity": "Low",
            "severity_color": "#6b7280",
            "description": "Baktığım şeyin eğittiğim bitki yapraklarından biri olduğuna pek emin olamadım. Kamera yapraktan çok başka nesnelere veya karmaşık bir arka plana odaklanmış olabilir.",
            "symptoms": ["Görüntüde net bir hastalık algılanamadı, AI kararsız kaldı.", "Kadraja insan eli, saksı, eşya veya çoklu yapraklar girmiş olabilir."],
            "treatment": ["Lütfen sadece TEK bir yaprağı kameranın merkeze (kare içine) yaklaştırıp netlemesini bekleyin.", "Arka planın sade ve tek renk (toprak/siyah/beyaz) olmasına özen gösterin."],
            "model": "system_guard"
        }
        return not_a_leaf_result, all_candidates[:4]
    
    return top_result, all_candidates[:5]


def get_demo_result():
    """Model yokken demo sonuç döndür."""
    demo_class = "Tomato___Early_blight"
    info = get_disease_info(demo_class)
    top = {
        "class": demo_class, "confidence": 0.9412, "confidence_pct": 94.12,
        "name": info["name"], "emoji": info["emoji"],
        "severity": info["severity"], "severity_color": get_severity_color(info["severity"]),
        "description": info["description"], "symptoms": info["symptoms"],
        "treatment": info["treatment"], "model": "demo",
    }
    others = [
        {"class": "Tomato___Late_blight", "confidence": 0.032, "confidence_pct": 3.2,
         "name": "Domates - Geç Yanıklık", "emoji": "🍅"},
        {"class": "Tomato___Septoria_leaf_spot", "confidence": 0.018, "confidence_pct": 1.8,
         "name": "Domates - Septoria Leke", "emoji": "🍅"},
    ]
    return top, [top] + others


# ─── Rotalar ───────────────────────────────────────────────────────────────
@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

@app.route("/")
def index():
    model_ready = len(models) > 0
    num_classes = sum(len(m["class_names"]) for m in models.values())
    num_models = len(models)
    return render_template("index.html", model_ready=model_ready,
                         num_classes=num_classes, num_models=num_models)


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files["file"]
    if not file.filename:
        return jsonify({"error": "Dosya seçilmedi"}), 400

    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "webp", "bmp"}:
        return jsonify({"error": "Desteklenmeyen dosya formatı."}), 400

    try:
        image_bytes = file.read()

        if models:
            top_result, all_results = make_prediction(image_bytes)
            demo_mode = False
        else:
            top_result, all_results = get_demo_result()
            demo_mode = True

        img_b64 = base64.b64encode(image_bytes).decode("utf-8")
        img_mime = f"image/{ext if ext != 'jpg' else 'jpeg'}"

        return jsonify({
            "success": True, "demo_mode": demo_mode,
            "top": top_result, "all": all_results,
            "image_b64": img_b64, "image_mime": img_mime,
        })
    except Exception as e:
        return jsonify({"error": f"Tahmin hatası: {str(e)}"}), 500

# ─── AGROBOT API (Gemini Entegrasyonu) ────────────────────────────────────────────────
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Mesaj boş olamaz."}), 400

    user_message = data["message"]
    context = data.get("context", "Bilinmeyen Durum")

    # Kullanıcıdan alınan Gemini API Key
    api_key = "AIzaSyBOQ7xBaDN53h38JYKc6Exss81xQcv-eCo"

    if not api_key:
        return jsonify({
            "reply": "⚠️ AgroBot'u kullanabilmek için bir **Gemini API Anahtarı** ayarlamanız gerekiyor. Lütfen geliştiriciye başvurup API Key isteyin veya kodu güncelleyin."
        })

    try:
        client = genai.Client(api_key=api_key)
        
        system_prompt = f"""
        Sen "AgroBot" adında uzman bir tarım ve ziraat mühendisi yapay zekasısın. 
        Kullanıcının bitkisine şu teşhis konuldu: '{context}'.
        Kullanıcının sorusuna kısa, yetkin, güven veren ve çözüm odaklı bir yanıt (Maksimum 3-4 cümle) ver. 
        Asla tıbbi bir insani tavsiye verme. Sadece bitkiler ve tarım üzerine konuş.
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,
            ),
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Gemini API Hatası: {e}")
        return jsonify({"error": "Yapay zeka servisine bağlanılamadı. Lütfen daha sonra tekrar deneyin."}), 500


@app.route("/predict_camera", methods=["POST"])
def predict_camera():
    try:
        data = request.get_json(force=True)
        if not data or "image" not in data:
            return jsonify({"error": "Görüntü verisi eksik"}), 400

        img_data = data["image"]
        if "," in img_data:
            img_data = img_data.split(",", 1)[1]
        image_bytes = base64.b64decode(img_data)

        if models:
            top_result, all_results = make_prediction(image_bytes)
            demo_mode = False
        else:
            top_result, all_results = get_demo_result()
            demo_mode = True

        return jsonify({
            "success": True, "demo_mode": demo_mode,
            "top": top_result, "all": all_results,
        })
    except Exception as e:
        return jsonify({"error": f"Kamera tahmin hatası: {str(e)}"}), 500


@app.route("/status")
def status():
    model_info = {}
    for name, m in models.items():
        model_info[name] = {
            "num_classes": len(m["class_names"]),
            "type": m.get("type", "onnx"),
        }
    return jsonify({
        "models_loaded": len(models),
        "model_info": model_info,
        "total_classes": sum(len(m["class_names"]) for m in models.values()),
    })


@app.route("/classes")
def classes():
    result = []
    for model_name, m in models.items():
        for cn in m["class_names"]:
            info = get_disease_info(cn)
            result.append({"class": cn, "name": info["name"],
                          "emoji": info["emoji"], "model": model_name})
    return jsonify(result)


# ─── Modelleri Yükle (Gunicorn/Üretim ortamı için) ──────────────────────────
load_models()

# ─── Başlat (Yerel Geliştirme İçin) ────────────────────────────────────────
if __name__ == "__main__":
    print("\n🌿 AgroAI — Bitki Hastalığı Tespiti")
    if models:
        for name, m in models.items():
            icon = "🌾" if name == "plant" else "🏠"
            print(f"   {icon} {name}: {len(m['class_names'])} sınıf")
        total = sum(len(m["class_names"]) for m in models.values())
        print(f"   📊 Toplam: {total} sınıf, {len(models)} model")
    else:
        print("   🔴 Demo modunda")
    print("   → http://localhost:8080\n")
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=False)
