import { NavLink, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { checkOllamaStatus } from '../services/api';

export default function TopNav() {
  const [ollamaStatus, setOllamaStatus] = useState({ available: false, model: null, checking: true });
  const navigate = useNavigate();

  useEffect(() => {
    checkOllamaStatus()
      .then((res) => setOllamaStatus({ ...res, checking: false }))
      .catch(() => setOllamaStatus({ available: false, model: null, checking: false }));
  }, []);

  let statusLabel = 'Checking...';
  let dotClass = '';
  
  if (!ollamaStatus.checking) {
    if (ollamaStatus.available) {
      statusLabel = 'OLLAMA: Connected';
      dotClass = 'live';
    } else {
      statusLabel = 'OLLAMA: Unavailable — Local NLP active';
      dotClass = 'demo';
    }
  }

  return (
    <nav className="topnav" role="navigation" aria-label="Main navigation">
      <div className="topnav-inner">
        <button
          className="topnav-brand"
          onClick={() => navigate('/')}
          style={{ cursor: 'pointer', background: 'none', border: 'none' }}
          aria-label="CyberGuard home"
        >
          <span className="topnav-logo">CyberGuard</span>
          <span className="topnav-tagline">Prototype cybersecurity awareness tool</span>
        </button>

        <div className="topnav-right">
          <div className="topnav-links">
            <NavLink
              to="/"
              end
              className={({ isActive }) => `topnav-link${isActive ? ' active' : ''}`}
            >
              Analyze
            </NavLink>
            <NavLink
              to="/history"
              className={({ isActive }) => `topnav-link${isActive ? ' active' : ''}`}
            >
              History
            </NavLink>
            <NavLink
              to="/guide"
              className={({ isActive }) => `topnav-link${isActive ? ' active' : ''}`}
            >
              Security Guide
            </NavLink>
            <NavLink
              to="/about"
              className={({ isActive }) => `topnav-link${isActive ? ' active' : ''}`}
            >
              About
            </NavLink>
          </div>

          <div
            className="status-indicator"
            role="status"
            aria-label={`System status: ${statusLabel}`}
            onClick={() => {
              if (window.confirm("Open Developer Settings?")) {
                const url = prompt("Ollama URL:", "http://localhost:11434");
                const model = prompt("Ollama Model:", "llama3.2:3b");
                if (url && model) {
                  fetch('/api/ollama/config', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url, model, enabled: true })
                  }).then(() => window.location.reload());
                }
              }
            }}
            style={{ cursor: 'pointer' }}
            title="Click to configure Ollama"
          >
            <span className={`status-dot ${dotClass}`} />
            {statusLabel}
          </div>
        </div>
      </div>
    </nav>
  );
}
