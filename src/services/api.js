const RAW_BASE = import.meta.env.VITE_API_URL 
  || (import.meta.env.DEV ? 'http://localhost:8000/api' : '/api');
const BASE = RAW_BASE.replace(/\/+$/, '');

async function request(path, options = {}) {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const res = await fetch(`${BASE}${normalizedPath}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });

  if (!res.ok) {
    let detail = `Request failed (${res.status})`;
    try {
      const body = await res.json();
      if (body.detail) detail = body.detail;
    } catch (_) { /* ignore */ }
    throw new Error(detail);
  }

  return res.json();
}

export async function checkHealth() {
  return request('/health');
}

export async function analyzeMessage(message, demoMode = false) {
  return request('/analyze', {
    method: 'POST',
    body: JSON.stringify({ message, demo_mode: demoMode }),
  });
}

export async function sendChatMessage(question, analysisContext) {
  return request('/chat', {
    method: 'POST',
    body: JSON.stringify({ question, analysis_context: analysisContext }),
  });
}
