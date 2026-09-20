import { useNavigate } from 'react-router-dom';
import { useHistory } from '../hooks/useHistory';
import HistoryList from '../components/HistoryList';

export default function HistoryPage() {
  const navigate = useNavigate();
  const { entries, refresh, clear } = useHistory();

  function handleSelect(entry) {
    // Navigate to analyze page and restore the analysis via session storage
    sessionStorage.setItem('cyberguard_restore', JSON.stringify(entry));
    navigate('/');
  }

  function handleClear() {
    if (window.confirm('Clear all history? This cannot be undone.')) {
      clear();
    }
  }

  return (
    <main className="page-content">
      <div style={{ maxWidth: '720px' }}>
        <div className="analyze-header">
          <h1 className="analyze-title">History</h1>
          <p className="analyze-subtitle">
            Recent analyses are stored locally in your browser.
          </p>
        </div>

        <HistoryList
          entries={entries}
          onSelect={handleSelect}
          onClear={handleClear}
        />
      </div>
    </main>
  );
}
