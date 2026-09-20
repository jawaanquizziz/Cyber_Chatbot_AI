import { SECURITY_GUIDE } from '../data/securityGuide';
import SecurityTipCard from '../components/SecurityTipCard';

export default function SecurityGuidePage() {
  return (
    <main className="page-content">
      <div style={{ maxWidth: '720px' }}>
        <div className="analyze-header">
          <h1 className="analyze-title">Security Guide</h1>
          <p className="analyze-subtitle">
            Reference information on common message-based threats and how to respond safely.
          </p>
        </div>

        <div style={{ marginTop: 'var(--space-6)' }}>
          {SECURITY_GUIDE.map((item) => (
            <SecurityTipCard key={item.key} item={item} />
          ))}
        </div>

        <div
          className="card card-sm"
          style={{ marginTop: 'var(--space-6)', color: 'var(--text-muted)', fontSize: '0.8125rem', lineHeight: 1.6 }}
        >
          <p style={{ fontWeight: 600, color: 'var(--text)', marginBottom: 'var(--space-2)' }}>
            Report cybercrime in India
          </p>
          <p>
            You can report cybercrime incidents at{' '}
            <strong>cybercrime.gov.in</strong> or call the national helpline{' '}
            <strong>1930</strong>.
          </p>
        </div>
      </div>
    </main>
  );
}
