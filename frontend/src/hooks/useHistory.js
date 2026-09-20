import { useState, useCallback } from 'react';
import { getHistory, clearHistory } from '../services/history';

export function useHistory() {
  const [entries, setEntries] = useState(() => getHistory());

  const refresh = useCallback(() => {
    setEntries(getHistory());
  }, []);

  const clear = useCallback(() => {
    clearHistory();
    setEntries([]);
  }, []);

  return { entries, refresh, clear };
}
