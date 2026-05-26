/**
 * AGRINOVA Service Worker
 * Enables offline functionality, caching, and background sync
 */

const CACHE_NAME = 'agrinova-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/css/style.css',
  '/css/responsive.css',
  '/css/animations.css',
  '/js/main.js',
  '/js/crop.js',
  '/js/weather.js',
  '/js/prices.js',
  '/js/schemes.js',
  '/js/chatbot.js'
];

// Install Event - Cache essential assets
self.addEventListener('install', (event) => {
  console.log('🌾 Service Worker Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('🌾 Caching essential assets...');
      return cache.addAll(ASSETS_TO_CACHE).catch(err => {
        console.log('⚠️ Could not cache all assets, continuing with partial cache:', err);
        return cache.addAll(ASSETS_TO_CACHE.filter(url => url === '/' || url === '/index.html'));
      });
    })
  );
  
  self.skipWaiting();
});

// Activate Event - Clean up old caches
self.addEventListener('activate', (event) => {
  console.log('🌾 Service Worker Activating...');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('🌾 Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  
  self.clients.claim();
});

// Fetch Event - Serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Skip non-GET requests
  if (event.request.method !== 'GET') {
    return;
  }

  // Handle API requests differently
  if (event.request.url.includes('/api/')) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          // Clone the response
          const clonedResponse = response.clone();
          
          // Cache successful API responses
          if (response.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, clonedResponse);
            });
          }
          
          return response;
        })
        .catch(() => {
          // Return cached response or offline page
          return caches.match(event.request)
            .then(cachedResponse => cachedResponse || createOfflinePage());
        })
    );
  } else {
    // For static assets, try cache first, then network
    event.respondWith(
      caches.match(event.request)
        .then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }

          return fetch(event.request).then((response) => {
            // Cache successful responses
            if (!response || response.status !== 200 || response.type === 'error') {
              return response;
            }

            const clonedResponse = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, clonedResponse);
            });

            return response;
          })
          .catch(() => {
            // Return offline page for navigation requests
            if (event.request.mode === 'navigate') {
              return createOfflinePage();
            }
            
            // Return a generic offline response
            return new Response('Offline - Please check your internet connection', {
              status: 503,
              statusText: 'Service Unavailable',
              headers: new Headers({
                'Content-Type': 'text/plain'
              })
            });
          });
        })
    );
  }
});

// Create offline page
function createOfflinePage() {
  return new Response(`
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>AGRINOVA - Offline</title>
      <style>
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        
        body {
          font-family: 'Poppins', sans-serif;
          background: linear-gradient(135deg, #f5f7fa 0%, #e9f2e9 100%);
          display: flex;
          justify-content: center;
          align-items: center;
          min-height: 100vh;
          color: #1a2a1a;
        }
        
        .offline-container {
          text-align: center;
          padding: 40px;
          background: white;
          border-radius: 15px;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
          max-width: 500px;
        }
        
        .offline-icon {
          font-size: 4rem;
          margin-bottom: 20px;
          animation: pulse 2s infinite;
        }
        
        h1 {
          color: #2e7d32;
          margin-bottom: 15px;
          font-size: 2rem;
        }
        
        p {
          color: #555;
          margin-bottom: 20px;
          line-height: 1.6;
        }
        
        .offline-tips {
          background: #e8f5e9;
          padding: 20px;
          border-radius: 10px;
          text-align: left;
          margin-top: 20px;
        }
        
        .offline-tips h3 {
          color: #2e7d32;
          margin-bottom: 10px;
        }
        
        .offline-tips ul {
          list-style: none;
          padding-left: 0;
        }
        
        .offline-tips li {
          padding: 5px 0;
          color: #333;
        }
        
        .offline-tips li:before {
          content: "✓ ";
          color: #4caf50;
          font-weight: bold;
          margin-right: 8px;
        }
        
        button {
          background: #2e7d32;
          color: white;
          border: none;
          padding: 12px 30px;
          border-radius: 5px;
          cursor: pointer;
          font-size: 1rem;
          margin-top: 20px;
          transition: background 0.3s;
        }
        
        button:hover {
          background: #1b5e20;
        }
        
        @keyframes pulse {
          0%, 100% { transform: scale(1); }
          50% { transform: scale(1.1); }
        }
      </style>
    </head>
    <body>
      <div class="offline-container">
        <div class="offline-icon">🌾</div>
        <h1>You're Offline</h1>
        <p>AGRINOVA is currently unavailable because you're not connected to the internet.</p>
        
        <div class="offline-tips">
          <h3>What you can do:</h3>
          <ul>
            <li>Check your internet connection</li>
            <li>Review previously cached data</li>
            <li>Try again when online</li>
            <li>Save crop recommendations for later</li>
          </ul>
        </div>
        
        <button onclick="location.reload()">Retry Connection</button>
        <button onclick="location.href='/'">Go to Home</button>
      </div>
      
      <script>
        // Auto-retry connection
        window.addEventListener('online', () => {
          location.reload();
        });
        
        // Periodic connection check
        setInterval(() => {
          fetch('/').then(() => {
            console.log('Connection restored');
            setTimeout(() => location.reload(), 1000);
          }).catch(() => {
            console.log('Still offline');
          });
        }, 5000);
      </script>
    </body>
    </html>
  `, {
    headers: { 'Content-Type': 'text/html' }
  });
}

// Handle push notifications
self.addEventListener('push', (event) => {
  if (!event.data) return;

  const data = event.data.json();
  const options = {
    body: data.body || 'New notification from AGRINOVA',
    icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><rect fill="%232e7d32" width="192" height="192"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="120" fill="white" font-weight="bold">🌾</text></svg>',
    badge: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><rect fill="%232e7d32" width="192" height="192"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="120" fill="white">🌾</text></svg>',
    tag: data.tag || 'agrinova-notification',
    requireInteraction: data.requireInteraction || false,
    data: data
  };

  event.waitUntil(
    self.registration.showNotification('AGRINOVA', options)
  );
});

// Handle notification clicks
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true })
      .then((clientList) => {
        // Check if window is already open
        for (let i = 0; i < clientList.length; i++) {
          const client = clientList[i];
          if (client.url === '/' && 'focus' in client) {
            return client.focus();
          }
        }
        // Open new window if not found
        if (clients.openWindow) {
          return clients.openWindow(event.notification.data.url || '/');
        }
      })
  );
});

// Message handler for communication with clients
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CACHE_DATA') {
    caches.open(CACHE_NAME).then((cache) => {
      cache.put(event.data.url, new Response(JSON.stringify(event.data.data)));
    });
  }
});

console.log('🌾 AGRINOVA Service Worker loaded');
