const CACHE_NAME = 'agroai-cache-v2';
const ASSETS = [
    '/',
    '/static/style.css',
    '/static/app.js',
    '/static/manifest.json',
    '/static/icons/icon-512x512.svg',
    'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;700&display=swap'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(ASSETS))
    );
});

self.addEventListener('fetch', event => {
    // Sadece GET isteklerini önbellekle (POST veya fotoğraf kamerası isteklerini engelleme)
    if (event.request.method !== 'GET') return;

    event.respondWith(
        fetch(event.request)
            .then(response => {
                // Ağdan başarılı yanıt aldıysak döndür (Dynamic render her zaman güncel kalsın)
                return response;
            })
            .catch(() => {
                // Ağ yoksa (çevrimdışı) cache'ten döndür
                return caches.match(event.request);
            })
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(keys
                .filter(key => key !== CACHE_NAME)
                .map(key => caches.delete(key))
            );
        })
    );
});
