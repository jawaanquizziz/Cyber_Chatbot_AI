const KEY = 'cyberguard_history';
const MAX_ENTRIES = 50;

export function getHistory() {
  try {
    return JSON.parse(localStorage.getItem(KEY) || '[]');
  } catch {
    return [];
  }
}

export function addHistoryEntry(message, analysis) {
  const entries = getHistory();
  const entry = {
    id: Date.now().toString(),
    timestamp: new Date().toISOString(),
    messagePreview: message.slice(0, 120),
    category: analysis.category,
    risk_level: analysis.risk_level,
    message,
    analysis,
  };
  const updated = [entry, ...entries].slice(0, MAX_ENTRIES);
  localStorage.setItem(KEY, JSON.stringify(updated));
  return entry;
}

export function clearHistory() {
  localStorage.removeItem(KEY);
}
