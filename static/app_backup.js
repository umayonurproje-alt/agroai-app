// ════════════════════════════════════════════════════════
//  AgroAI - Frontend JS
//  Kamera modu + Dosya yükleme modu
// ════════════════════════════════════════════════════════

// ── State ─────────────────────────────────────────────────────────────────
let selectedFile = null;
let cameraStream = null;
let cameraDevices = [];
let activeDeviceId = null;
let autoMode = false;
let autoInterval = null;
let isAnalyzing = false;
let currentTab = 'camera';

// ── Tab Geçişi ─────────────────────────────────────────────────────────────
function switchTab(tab) {
  currentTab = tab;
  const camSection = document.getElementById('cameraSection');
  const uploadSection = document.getElementById('uploadSection');
  const tabCamera = document.getElementById('tabCamera');
  const tabUpload = document.getElementById('tabUpload');

  if (tab === 'camera') {
    camSection.style.display = 'block';
    uploadSection.style.display = 'none';
    tabCamera.classList.add('tab-active');
    tabUpload.classList.remove('tab-active');
  } else {
    // Kamera sekmesinden çıkınca kamerayı durdur
    stopCamera();
    camSection.style.display = 'none';
    uploadSection.style.display = 'block';
    tabCamera.classList.remove('tab-active');
    tabUpload.classList.add('tab-active');
  }
  document.getElementById('resultSection').style.display = 'none';
  document.getElementById('loadingCard').style.display = 'none';
}

// ════════════════════════════════════════════════════════
//  KAMERA İŞLEVLERİ
// ════════════════════════════════════════════════════════

async function startCamera() {
  try {
    // Mevcut stream varsa kapat
    if (cameraStream) stopCamera(false);

    const constraints = {
      video: {
        deviceId: activeDeviceId ? { exact: activeDeviceId } : undefined,
        width: { ideal: 1280 },
        height: { ideal: 720 },
        facingMode: 'environment',   // Arka kamera tercih edilir (mobil)
      }
    };

    cameraStream = await navigator.mediaDevices.getUserMedia(constraints);

    const video = document.getElementById('cameraFeed');
    video.srcObject = cameraStream;

    // Kamera listesini doldur
    await populateCameraList();

    // UI göster
    document.getElementById('camIdle').style.display = 'none';
    document.getElementById('camError').style.display = 'none';
    document.getElementById('camActive').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';

  } catch (err) {
    console.error('Kamera hatası:', err);
    document.getElementById('camIdle').style.display = 'none';
    document.getElementById('camError').style.display = 'block';
    document.getElementById('camActive').style.display = 'none';
  }
}

async function populateCameraList() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    cameraDevices = devices.filter(d => d.kind === 'videoinput');
    const sel = document.getElementById('cameraSelect');
    sel.innerHTML = '';

    const track = cameraStream?.getVideoTracks()[0];
    const currentId = track?.getSettings()?.deviceId;

    cameraDevices.forEach((dev, i) => {
      const opt = document.createElement('option');
      opt.value = dev.deviceId;
      opt.textContent = dev.label || `Kamera ${i + 1}`;
      if (dev.deviceId === currentId) opt.selected = true;
      sel.appendChild(opt);
    });
  } catch (e) {
    console.warn('Kamera listesi alınamadı:', e);
  }
}

async function changeCamera() {
  const sel = document.getElementById('cameraSelect');
  activeDeviceId = sel.value;
  await startCamera();
}

function stopCamera(showIdle = true) {
  // Otomatik modu kapat
  setAutoMode(false);

  if (cameraStream) {
    cameraStream.getTracks().forEach(t => t.stop());
    cameraStream = null;
  }
  const video = document.getElementById('cameraFeed');
  if (video) video.srcObject = null;

  if (showIdle) {
    document.getElementById('camIdle').style.display = 'flex';
    document.getElementById('camActive').style.display = 'none';
  }
}

// ── Otomatik Mod ──────────────────────────────────────────────────────────
function toggleAutoMode() {
  setAutoMode(!autoMode);
}

function setAutoMode(on) {
  autoMode = on;
  const btn = document.getElementById('autoToggle');
  const label = document.getElementById('camModeLabel');

  if (on) {
    btn.classList.add('toggle-on');
    label.textContent = '🔄 Otomatik mod — 2 sn\'de bir analiz';
    autoInterval = setInterval(() => {
      if (!isAnalyzing) captureAndAnalyze(true);
    }, 2000);
  } else {
    btn.classList.remove('toggle-on');
    label.textContent = 'Manuel mod — butona basın';
    clearInterval(autoInterval);
    autoInterval = null;
  }
}

// ── Kare Yakala ve Analiz Et ──────────────────────────────────────────────
async function captureAndAnalyze(silent = false) {
  if (isAnalyzing || !cameraStream) return;
  isAnalyzing = true;

  const video = document.getElementById('cameraFeed');
  const canvas = document.getElementById('captureCanvas');
  canvas.width = video.videoWidth || 640;
  canvas.height = video.videoHeight || 480;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Tarama animasyonu
  if (!silent) showScanAnimation();

  // Base64 JPEG
  const b64 = canvas.toDataURL('image/jpeg', 0.92);

  try {
    if (!silent) {
      document.getElementById('loadingCard').style.display = 'block';
      document.getElementById('resultSection').style.display = 'none';
    }

    const res = await fetch('/predict_camera', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image: b64 }),
    });
    const data = await res.json();

    if (!silent) document.getElementById('loadingCard').style.display = 'none';
    hideScanAnimation();

    if (!res.ok || data.error) throw new Error(data.error || 'Sunucu hatası');

    // Frame görüntüsü olarak kaydet (result kartı için)
    data.image_b64 = b64.split(',')[1];
    data.image_mime = 'image/jpeg';

    renderResult(data);

  } catch (err) {
    hideScanAnimation();
    if (!silent) {
      document.getElementById('loadingCard').style.display = 'none';
      showToast(`❌ ${err.message}`, 'error');
    }
  } finally {
    isAnalyzing = false;
  }
}

function showScanAnimation() {
  const line = document.getElementById('scanLine');
  const hint = document.getElementById('camHint');
  if (line) line.style.display = 'block';
  if (hint) hint.textContent = 'Analiz ediliyor...';
}

function hideScanAnimation() {
  const line = document.getElementById('scanLine');
  const hint = document.getElementById('camHint');
  if (line) line.style.display = 'none';
  if (hint) hint.textContent = 'Yaprağı çerçeve içine getirin';
}

// ════════════════════════════════════════════════════════
//  DOSYA YÜKLEME İŞLEVLERİ
// ════════════════════════════════════════════════════════

function handleDragOver(e) {
  e.preventDefault();
  document.getElementById('dropZone').classList.add('drag-over');
}
function handleDragLeave(e) {
  e.preventDefault();
  document.getElementById('dropZone').classList.remove('drag-over');
}
function handleDrop(e) {
  e.preventDefault();
  document.getElementById('dropZone').classList.remove('drag-over');
  const file = e.dataTransfer.files[0];
  if (file) loadFile(file);
}
function handleFileSelect(e) {
  const file = e.target.files[0];
  if (file) loadFile(file);
}

function loadFile(file) {
  const allowed = ['image/jpeg', 'image/png', 'image/webp', 'image/bmp'];
  if (!allowed.includes(file.type)) {
    showToast('❌ Desteklenmeyen format. JPG, PNG veya WEBP kullanın.', 'error'); return;
  }
  if (file.size > 16 * 1024 * 1024) {
    showToast('❌ Dosya 16 MB\'dan büyük.', 'error'); return;
  }
  selectedFile = file;
  const reader = new FileReader();
  reader.onload = (e) => {
    const img = document.getElementById('previewImg');
    img.src = e.target.result;
    img.style.opacity = '0';
    document.getElementById('dropZone').style.display = 'none';
    document.getElementById('previewArea').style.display = 'block';
    document.getElementById('previewName').textContent = file.name;
    document.getElementById('resultSection').style.display = 'none';
    setTimeout(() => { img.style.transition = 'opacity 0.4s'; img.style.opacity = '1'; }, 50);
  };
  reader.readAsDataURL(file);
}

function clearImage() {
  selectedFile = null;
  document.getElementById('fileInput').value = '';
  document.getElementById('dropZone').style.display = 'flex';
  document.getElementById('previewArea').style.display = 'none';
  document.getElementById('resultSection').style.display = 'none';
  document.getElementById('loadingCard').style.display = 'none';
  document.getElementById('previewImg').src = '';
}

async function analyzeFile() {
  if (!selectedFile) return;
  document.getElementById('loadingCard').style.display = 'block';
  document.getElementById('resultSection').style.display = 'none';

  try {
    const formData = new FormData();
    formData.append('file', selectedFile);

    const res = await fetch('/predict', { method: 'POST', body: formData });
    const data = await res.json();

    document.getElementById('loadingCard').style.display = 'none';
    if (!res.ok || data.error) throw new Error(data.error || 'Sunucu hatası');
    renderResult(data);
  } catch (err) {
    document.getElementById('loadingCard').style.display = 'none';
    showToast(`❌ Hata: ${err.message}`, 'error');
  }
}

// ════════════════════════════════════════════════════════
//  SONUÇ GÖSTERİMİ
// ════════════════════════════════════════════════════════

function renderResult(data) {
  const top = data.top;

  document.getElementById('demoBanner').style.display = data.demo_mode ? 'flex' : 'none';

  // Yakalanan görüntüyü göster
  if (data.image_b64) {
    const mime = data.image_mime || 'image/jpeg';
    document.getElementById('resultImg').src = `data:${mime};base64,${data.image_b64}`;
  }

  document.getElementById('resultEmoji').textContent = top.emoji || '🌿';
  document.getElementById('resultName').textContent = top.name;

  // Severity badge
  const sevBadge = document.getElementById('severityBadge');
  sevBadge.textContent = `Şiddet: ${top.severity}`;
  const sc = top.severity_color || severityColor(top.severity);
  sevBadge.style.background = hexToRgba(sc, 0.15);
  sevBadge.style.border = `1px solid ${hexToRgba(sc, 0.4)}`;
  sevBadge.style.color = sc;

  document.getElementById('confidenceBadge').textContent = `%${top.confidence_pct} Güven`;
  document.getElementById('confidenceText').textContent = `%${top.confidence_pct}`;

  // Confidence bar animasyonu
  const fill = document.getElementById('confidenceBarFill');
  fill.style.width = '0';
  setTimeout(() => { fill.style.width = `${top.confidence_pct}%`; }, 200);

  // Renk: düşük güven griye kayar
  const pct = top.confidence_pct;
  fill.style.background = pct >= 70
    ? 'linear-gradient(90deg,#16a34a,#4ade80)'
    : pct >= 40
      ? 'linear-gradient(90deg,#d97706,#fbbf24)'
      : 'linear-gradient(90deg,#dc2626,#f87171)';

  document.getElementById('resultDescription').textContent = top.description || '';

  // Belirtiler + Tedavi
  const grid = document.getElementById('detailGrid');
  grid.innerHTML = '';
  if (top.symptoms?.length) {
    grid.innerHTML += buildDetailPanel('🔍 Belirtiler', top.symptoms, 'detail-panel-symptoms');
  }
  if (top.treatment?.length) {
    grid.innerHTML += buildDetailPanel('💊 Tedavi Önerileri', top.treatment, 'detail-panel-treatment');
  }

  // Top-5
  const list = document.getElementById('top5List');
  list.innerHTML = '';
  (data.all || []).slice(0, 5).forEach((item, idx) => {
    const pct = item.confidence_pct;
    const fill = idx === 0
      ? 'linear-gradient(90deg,#16a34a,#4ade80)'
      : 'linear-gradient(90deg,#0f766e,#14b8a6)';
    const li = document.createElement('li');
    li.className = 'top5-item';
    li.innerHTML = `
      <span class="top5-rank">${idx + 1}</span>
      <div class="top5-details">
        <div class="top5-bar-name">${item.emoji || ''} ${item.name || item.class}</div>
        <div class="top5-bar-bg">
          <div class="top5-bar-fill" id="bar-${idx}" style="background:${fill}"></div>
        </div>
      </div>
      <span class="top5-pct">%${pct}</span>`;
    list.appendChild(li);
    setTimeout(() => {
      const b = document.getElementById(`bar-${idx}`);
      if (b) b.style.width = `${pct}%`;
    }, 300 + idx * 80);
  });

  document.getElementById('resultSection').style.display = 'block';
  setTimeout(() => {
    document.getElementById('resultSection').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 100);
}

function buildDetailPanel(title, items, cls) {
  return `
    <div class="detail-panel ${cls}">
      <div class="detail-panel-title">${title}</div>
      <ul class="detail-list">${items.map(i => `<li>${i}</li>`).join('')}</ul>
    </div>`;
}

function resetResult() {
  document.getElementById('resultSection').style.display = 'none';
  if (currentTab === 'camera') {
    // Kamera hâlâ aktif, sadece sonucu gizle
  } else {
    clearImage();
  }
}

// ════════════════════════════════════════════════════════
//  PDF RAPOR OLUŞTURMA (Native Print)
// ════════════════════════════════════════════════════════
function downloadPDF() {
  // Sistem yazdır penceresini açar. 
  // Arka planda style.css içindeki "@media print" kuralları devrede olur
  window.print();
}

// ════════════════════════════════════════════════════════
//  YARDIMCI FONKSİYONLAR
// ════════════════════════════════════════════════════════
function severityColor(sev) {
  return { 'Yok': '#22c55e', 'Orta': '#f59e0b', 'Yüksek': '#ef4444', 'Çok Yüksek': '#dc2626' }[sev] || '#6b7280';
}
function hexToRgba(hex, a) {
  if (!hex?.startsWith('#')) return `rgba(107,114,128,${a})`;
  const r = parseInt(hex.slice(1, 3), 16),
    g = parseInt(hex.slice(3, 5), 16),
    b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r},${g},${b},${a})`;
}
function showToast(msg, type = 'info') {
  document.getElementById('toast')?.remove();
  const t = document.createElement('div');
  t.id = 'toast';
  const bg = type === 'error' ? 'rgba(239,68,68,0.95)' : 'rgba(34,197,94,0.95)';
  t.style.cssText = `position:fixed;bottom:28px;left:50%;transform:translateX(-50%);
    background:${bg};color:white;padding:12px 24px;border-radius:999px;
    font-weight:600;font-size:0.9rem;z-index:9999;
    box-shadow:0 8px 32px rgba(0,0,0,0.4);`;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => { t.style.transition = 'opacity 0.3s'; t.style.opacity = '0'; setTimeout(() => t.remove(), 300); }, 4000);
}

// Sayfa kapanırken kamerayı kapat
window.addEventListener('beforeunload', () => stopCamera(false));
