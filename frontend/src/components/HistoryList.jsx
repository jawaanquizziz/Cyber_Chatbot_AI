import RiskBadge from './RiskBadge';

function formatDate(isoString) {
  const d = new Date(isoString);
  return d.toLocaleDateString('en-IN', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true,
  });
}

export default function HistoryList({ entries, onSelect, onClear }) {
  if (entries.length === 0) {
    return (
      <div className="empty-state" style={{ padding: 'var(--space-10) var(--space-6)' }}>
        <p className="empty-title">No history yet</p>
        <p className="empty-desc">
          Analyses you run will appear here. They are stored locally in your browser.
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <p className="text-sm text-muted">{entries.length} recent {entries.length === 1 ? 'analysis' : 'analyses'}</p>
        <button
          id="clear-history-btn"
          className="btn btn-ghost btn-sm"
          onClick={onClear}
          aria-label="Clear all history"
        >
          Clear history
        </button>
      </div>

      <div>
        {entries.map((entry) => (
          <button
            key={entry.id}
            className="history-item"
            onClick={() => onSelect(entry)}
            aria-label={`Open analysis: ${entry.messagePreview}`}
            style={{ width: '100%', textAlign: 'left', cursor: 'pointer', font: 'inherit' }}
          >
            <div className="history-preview">
              <p className="history-message-preview">{entry.messagePreview}</p>
              <p className="history-meta">{formatDate(entry.timestamp)}</p>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 'var(--space-2)', flexShrink: 0 }}>
              <RiskBadge level={entry.risk_level} />
              <p className="text-xs text-muted">{entry.category}</p>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
