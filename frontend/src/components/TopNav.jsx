import { NavLink, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { checkHealth } from '../services/api';

export default function TopNav() {
  const [status, setStatus] = useState({ mode: 'checking', api_configured: false });
  const navigate = useNavigate();

  useEffect(() => {
    checkHealth()
      .then(setStatus)
      .catch(() => setStatus({ mode: 'offline', api_configured: false }));
  }, []);

  const dotClass =
    status.mode === 'live' ? '' : status.mode === 'demo' ? 'demo' : 'offline';

  const statusLabel =
    status.mode === 'live'
      ? 'Live'
      : status.mode === 'demo'
      ? 'Demo Mode'
      : status.mode === 'checking'
      ? 'Connecting...'
      : 'Offline';

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
          <span className="topnav-tagline">Message Security Analysis</span>
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
          >
            <span className={`status-dot ${dotClass}`} />
            {statusLabel}
          </div>
        </div>
      </div>

      {status.mode === 'demo' && (
        <div className="demo-banner" role="alert">
          Running in Demo Mode — add a Gemini API key to enable live analysis
        </div>
      )}
    </nav>
  );
}
