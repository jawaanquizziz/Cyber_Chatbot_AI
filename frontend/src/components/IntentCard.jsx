export default function IntentCard({ intent, explanation }) {
  if (!intent) return null;
  return (
    <div>
      <p className="section-label">Detected intent</p>
      <p
        style={{
          fontFamily: 'var(--font-mono)',
          fontSize: '0.875rem',
          color: 'var(--text)',
          fontWeight: 500,
          marginBottom: 'var(--space-2)',
        }}
      >
        {intent}
      </p>
      {explanation && (
        <p className="text-sm text-muted" style={{ lineHeight: 1.6 }}>
          {explanation}
        </p>
      )}
    </div>
  );
}
