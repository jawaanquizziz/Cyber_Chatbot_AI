import { useState } from 'react';

export default function SecurityTipCard({ item }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="guide-card">
      <button
        className="guide-card-header"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        aria-controls={`guide-${item.key}`}
        id={`guide-header-${item.key}`}
      >
        <span style={{ fontSize: '1.1rem' }} aria-hidden="true">{item.icon}</span>
        <span className="guide-card-title">{item.title}</span>
        <span
          style={{
            marginLeft: 'auto',
            color: 'var(--text-subtle)',
            fontSize: '0.875rem',
            transition: 'transform 0.2s ease',
            transform: open ? 'rotate(180deg)' : 'rotate(0deg)',
          }}
          aria-hidden="true"
        >
          ▾
        </span>
      </button>

      {open && (
        <div
          className="guide-card-body"
          id={`guide-${item.key}`}
          role="region"
          aria-labelledby={`guide-header-${item.key}`}
        >
          <div className="guide-section">
            <p className="guide-section-label">What it is</p>
            <p className="guide-section-text">{item.definition}</p>
          </div>

          <div className="guide-section">
            <p className="guide-section-label">Common warning signs</p>
            <ul className="guide-indicators-list">
              {item.indicators.map((ind, i) => (
                <li className="guide-indicator-item" key={i}>{ind}</li>
              ))}
            </ul>
          </div>

          <div className="guide-section">
            <p className="guide-section-label">Safe response</p>
            <p className="guide-section-text">{item.safeResponse}</p>
          </div>

          <div className="guide-section">
            <p className="guide-section-label">Prevention</p>
            <p className="guide-section-text">{item.prevention}</p>
          </div>
        </div>
      )}
    </div>
  );
}
