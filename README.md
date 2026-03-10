# AgroAI - Yapay Zeka Destekli Bitki Hastalığı Tespiti

**38 bitki hastalığını** anında tespit eden, Türkçe tedavi önerileri sunan web uygulaması.  
EfficientNetB3 transfer learning · PlantVillage veri seti · Flask

---

## 🚀 Hızlı Başlangıç

### 1. Bağımlılıkları Yükle
```bash
cd /Users/umay/Downloads/archive
pip install -r requirements.txt
```

### 2a. Uygulamayı Başlat (Demo Mod — Model Olmadan)
```bash
python app.py
```
Tarayıcıda aç: **http://localhost:5000**

> Demo modunda örnek bir sonuç gösterilir. Gerçek tahmin için modeli eğitmeniz gerekir.

### 2b. Modeli Eğit (Tam İşlev)
```bash
python train.py
```
Eğitim tamamlanınca:
- `plant_disease_model.h5` oluşacak
- `training_history.png` eğitim grafikleri kaydedilecek
- Uygulamayı yeniden başlatırsanız model otomatik yüklenir

---

## 📁 Proje Yapısı

```
archive/
├── train.py                        # Model eğitim scripti (EfficientNetB3)
├── app.py                          # Flask web uygulaması
├── disease_info.py                 # 38 hastalık için Türkçe açıklamalar
├── requirements.txt                # Python bağımlılıkları
├── plant_disease_model.h5          # Eğitim sonrası oluşan model
├── class_names.txt                 # Eğitim sonrası oluşan sınıf listesi
├── training_history.png            # Eğitim grafikleri
├── templates/
│   └── index.html                  # Ana sayfa
├── static/
│   ├── style.css                   # Glassmorphism UI
│   └── app.js                      # Frontend JavaScript
├── New Plant Diseases Dataset(Augmented)/
│   └── .../ train/ & valid/        # 87K+ görüntü
└── test/test/                      # 33 test görüntüsü
```

---

## 🌿 Desteklenen Bitkiler ve Hastalıklar

| Bitki | Hastalıklar |
|-------|------------|
| 🍎 Elma | Apple Scab, Black Rot, Cedar Rust, Sağlıklı |
| 🍒 Kiraz | Külleme, Sağlıklı |
| 🌽 Mısır | Gri Yaprak Lekesi, Yaygın Pas, Kuzey Yanıklığı, Sağlıklı |
| 🍇 Üzüm | Siyah Çürüklük, Esca, Yaprak Yanıklığı, Sağlıklı |
| 🍊 Portakal | Turunçgil Yeşillenmesi (HLB) |
| 🍑 Şeftali | Bakteriyel Benek, Sağlıklı |
| 🫑 Biber | Bakteriyel Benek, Sağlıklı |
| 🥔 Patates | Erken Yanıklık, Geç Yanıklık, Sağlıklı |
| 🍓 Çilek | Yaprak Yanması, Sağlıklı |
| 🍅 Domates | 9 hastalık + Sağlıklı |
| + | Yaban Mersini, Ahududu, Soya, Kabak (Sağlıklı) |

---

## ⚡ Hız İpuçları

- **GPU varsa**: `train.py` içinde `BATCH_SIZE = 64` veya `128` yapın
- **Google Colab**: Veri setini Drive'a yükleyip GPU ile 2-3 saatte eğitin
- **Kaggle**: PlantVillage kernel'larından hazır modeli indirebilirsiniz

---

## 🔧 Model Mimarisi

```
EfficientNetB3 (ImageNet önceden eğitilmiş)
  ↓ GlobalAveragePooling2D
  ↓ BatchNormalization + Dropout(0.4)
  ↓ Dense(512, relu)
  ↓ BatchNormalization + Dropout(0.3)
  ↓ Dense(38, softmax)
```

**Eğitim stratejisi**: 2 faz
1. Temel model dondurulmuş → yeni katmanlar eğitilir
2. Fine-tuning → son 50 katman açılır, düşük learning rate ile eğitim
