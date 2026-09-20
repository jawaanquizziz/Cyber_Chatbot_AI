export default function EmptyState() {
  return (
    <div className="empty-state" role="status" aria-label="No analysis yet">
      <p className="empty-title">No analysis yet</p>
      <p className="empty-desc">
        Paste a message to begin. CyberGuard will identify possible intent,
        extracted entities, and security indicators.
      </p>
      <p className="empty-desc" style={{ marginTop: 'var(--space-4)', color: 'var(--text-subtle)' }}>
        Use the <strong style={{ color: 'var(--text-muted)' }}>Load example</strong> dropdown to
        try a sample message.
      </p>
    </div>
  );
}
