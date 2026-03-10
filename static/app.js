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
let currentDiseaseContext = ''; // AgroBot için o anki bağlam

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

  // Sadece ortadaki çerçeveyi almak için (Square Crop)
  const size = Math.min(video.videoWidth, video.videoHeight);
  const startX = (video.videoWidth - size) / 2;
  const startY = (video.videoHeight - size) / 2;

  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d');

  // (video_source, src_x, src_y, src_w, src_h, dest_x, dest_y, dest_w, dest_h)
  ctx.drawImage(video, startX, startY, size, size, 0, 0, size, size);

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
  const files = e.dataTransfer.files;
  if (files.length > 1) {
    analyzeBatch(files);
  } else if (files.length === 1) {
    loadFile(files[0]);
  }
}
function handleFileSelect(e) {
  const files = e.target.files;
  if (files.length > 1) {
    analyzeBatch(files);
  } else if (files.length === 1) {
    loadFile(files[0]);
  }
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
//  ÇOKLU ANALİZ (BATCH) İŞLEVLERİ
// ════════════════════════════════════════════════════════

async function analyzeBatch(files) {
  const allowed = ['image/jpeg', 'image/png', 'image/webp', 'image/bmp'];
  const validFiles = Array.from(files).filter(f => allowed.includes(f.type) && f.size <= 16 * 1024 * 1024);

  if (validFiles.length === 0) {
    showToast('❌ Geçerli formatta veya boyutta fotoğraf bulunamadı.', 'error');
    return;
  }

  // Arayüzü hazırla
  document.getElementById('dropZone').style.display = 'none';
  document.getElementById('resultSection').style.display = 'none';
  const batchSection = document.getElementById('batchResultSection');
  const tbody = document.getElementById('batchTableBody');

  batchSection.style.display = 'block';
  tbody.innerHTML = ''; // Tabloyu temizle

  // Tabloda her dosya için bekleyen satır oluştur
  const rows = {};
  for (let i = 0; i < validFiles.length; i++) {
    const file = validFiles[i];
    const tr = document.createElement('tr');
    tr.id = `batch-row-${i}`;
    tr.innerHTML = `
      <td><div class="batch-img-placeholder">⏳</div></td>
      <td class="batch-filename">${file.name}</td>
      <td id="batch-name-${i}">Analiz bekleniyor...</td>
      <td id="batch-score-${i}">-</td>
      <td id="batch-status-${i}">⏳ Bekliyor</td>
    `;
    tbody.appendChild(tr);
    rows[i] = { file, tr };
  }

  // Dosyaları sırayla sunucuya gönder
  for (let i = 0; i < validFiles.length; i++) {
    const rowId = i;
    const file = validFiles[i];

    document.getElementById(`batch-status-${rowId}`).innerHTML = '🔄 İşleniyor...';

    try {
      const formData = new FormData();
      formData.append('file', file);
      const res = await fetch('/predict', { method: 'POST', body: formData });
      const data = await res.json();

      if (!res.ok || data.error) throw new Error(data.error || 'Hata');

      const top = data.top;
      const mime = data.image_mime || 'image/jpeg';
      const imgSrc = data.image_b64 ? `data:${mime};base64,${data.image_b64}` : '';

      // Satırı güncelle
      const imgTd = imgSrc ? `<img src="${imgSrc}" class="batch-tb-img" />` : '🖼️';
      document.getElementById(`batch-row-${rowId}`).cells[0].innerHTML = imgTd;
      document.getElementById(`batch-name-${rowId}`).innerHTML = `${top.emoji || ''} ${top.name}`;
      document.getElementById(`batch-score-${rowId}`).innerHTML = `<span style="color:${top.confidence_pct > 65 ? '#10b981' : '#f59e0b'}">%${top.confidence_pct}</span>`;
      document.getElementById(`batch-status-${rowId}`).innerHTML = '✅ Tamamlandı';

      // Geçmişe de kaydet
      if (!data.demo_mode) saveToHistory(data);

    } catch (err) {
      document.getElementById(`batch-status-${rowId}`).innerHTML = `<span style="color:#ef4444">❌ Başarısız</span>`;
      document.getElementById(`batch-name-${rowId}`).innerHTML = 'Hata oluştu';
    }
  }
  showToast('✅ Çoklu analiz tamamlandı', 'success');
}

function downloadCSV() {
  const tbody = document.getElementById('batchTableBody');
  const rows = tbody.querySelectorAll('tr');
  if (rows.length === 0) {
    showToast('❌ İndirilecek veri yok', 'error'); return;
  }

  let csvContent = "data:text/csv;charset=utf-8,\uFEFF"; // Türkçe karakter desteği için BOM
  csvContent += "Dosya Adı;Hastalık Teşhisi;Güven Oranı;Durum\r\n"; // Başlık Satırı

  rows.forEach(tr => {
    const cols = tr.querySelectorAll('td');
    const fileName = cols[1].innerText;
    const diseaseName = cols[2].innerText;
    const score = cols[3].innerText.replace('%', ''); // Sadece rakam kalsın istenir
    const status = cols[4].innerText;

    // Noktalı virgül ile CSV satırı oluştur (Türkçe Excel genelde noktalı virgül bekler)
    csvContent += `"${fileName}";"${diseaseName}";"${score}";"${status}"\r\n`;
  });

  // Dosyayı indir
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  const dateStr = new Date().toISOString().split('T')[0];
  link.setAttribute("download", `AgroAI_Analiz_${dateStr}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ════════════════════════════════════════════════════════
//  SONUÇ GÖSTERİMİ
// ════════════════════════════════════════════════════════

function renderResult(data) {
  const top = data.top;

  // Analizi tarayıcı geçmişine (LocalStorage) kaydet
  if (!data.demo_mode) {
    saveToHistory(data);
  }

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

// ════════════════════════════════════════════════════════
//  AGROBOT (AI CHAT) MANTIKLARI
// ════════════════════════════════════════════════════════

function openAgroBot() {
  document.getElementById('agrobotOverlay').style.display = 'flex';
  document.getElementById('chatInput').focus();
}

function closeAgroBot(e, force = false) {
  if (force || e.target.id === 'agrobotOverlay') {
    document.getElementById('agrobotOverlay').style.display = 'none';
  }
}

function handleChatKeyPress(e) {
  if (e.key === 'Enter') {
    sendChatMessage();
  }
}

async function sendChatMessage() {
  const inputEl = document.getElementById('chatInput');
  const text = inputEl.value.trim();
  if (!text) return;

  // 1. Kullanıcı mesajını ekrana bas
  appendMessage(text, 'user');
  inputEl.value = '';

  // 2. Yükleniyor baloncuğu ekle
  const typingId = appendTypingIndicator();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        context: currentDiseaseContext
      })
    });

    const data = await res.json();
    removeMessage(typingId);

    // Eğer metin yoksa yanıt dönmedi demektir
    if (!res.ok) throw new Error(data.error || 'Bot yanıt veremedi.');

    // 3. Bot yanıtını ekrana bas
    appendMessage(data.reply, 'bot');

  } catch (err) {
    removeMessage(typingId);
    appendMessage(`❌ Hata: ${err.message}`, 'bot');
  }
}

function appendMessage(text, sender) {
  const container = document.getElementById('chatMessages');
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}-message`;

  // Markdown veya basit bold/br çevirisi
  let formattedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  formattedText = formattedText.replace(/\n/g, '<br>');

  msgDiv.innerHTML = `<div class="msg-bubble">${formattedText}</div>`;
  container.appendChild(msgDiv);
  container.scrollTop = container.scrollHeight;
  return msgDiv.id; // Sonradan silmek gerekirse
}

function appendTypingIndicator() {
  const container = document.getElementById('chatMessages');
  const id = 'typing-' + Date.now();
  const msgDiv = document.createElement('div');
  msgDiv.id = id;
  msgDiv.className = `message bot-message`;
  msgDiv.innerHTML = `<div class="msg-bubble"><span class="dots">...</span></div>`;
  container.appendChild(msgDiv);
  container.scrollTop = container.scrollHeight;
  return id;
}

function removeMessage(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

// ════════════════════════════════════════════════════════
//  GEÇMİŞ TARAMALAR (LOCAL STORAGE HISTORY)
// ════════════════════════════════════════════════════════

function openHistoryModal() {
  document.getElementById('historyOverlay').style.display = 'flex';
  loadHistory();
}

function closeHistoryModal(e, force = false) {
  if (force || e.target.id === 'historyOverlay') {
    document.getElementById('historyOverlay').style.display = 'none';
  }
}

function saveToHistory(data) {
  try {
    const top = data.top;

    // Bilinmeyen nesneleri geçmişe kaydetme
    if (top.class === "Unknown_Object") return;

    let history = JSON.parse(localStorage.getItem('agroai_history') || '[]');

    const newItem = {
      id: Date.now(),
      date: new Date().toLocaleString('tr-TR', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }),
      name: top.name,
      score: top.confidence_pct,
      image: data.image_b64 ? `data:${data.image_mime || 'image/jpeg'};base64,${data.image_b64}` : null
    };

    history.unshift(newItem); // En başa ekle

    // Max 10 kayıt tut
    if (history.length > 10) {
      history = history.slice(0, 10);
    }

    localStorage.setItem('agroai_history', JSON.stringify(history));
  } catch (e) {
    console.error("Geçmiş kaydedilemedi:", e);
  }
}

function loadHistory() {
  const list = document.getElementById('historyList');
  list.innerHTML = '';

  try {
    const history = JSON.parse(localStorage.getItem('agroai_history') || '[]');

    if (history.length === 0) {
      list.innerHTML = '<li class="history-empty">Henüz kaydedilmiş bir tarama yok.</li>';
      return;
    }

    history.forEach(item => {
      const li = document.createElement('li');
      li.className = 'history-item';

      const imgSrc = item.image ? item.image : 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="%239ca3af" viewBox="0 0 24 24"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>';

      li.innerHTML = `
        <img src="${imgSrc}" class="history-item-img" alt="${item.name}">
        <div class="history-item-info">
          <div class="history-item-date">${item.date}</div>
          <div class="history-item-name" title="${item.name}">${item.name}</div>
          <div class="history-item-score">%${item.score} Güven</div>
        </div>
      `;
      list.appendChild(li);
    });
  } catch (e) {
    console.error("Geçmiş okunamadı:", e);
    list.innerHTML = '<li class="history-empty">Geçmiş yüklenirken hata oluştu.</li>';
  }
}
