import { useState, useRef } from 'react';
import { EXAMPLES } from '../data/examples';

const MAX_CHARS = 5000;

export default function MessageInput({ onAnalyze, onDemoMode, loading }) {
  const [message, setMessage] = useState('');
  const textareaRef = useRef(null);

  const charCount = message.length;
  const isOverLimit = charCount > MAX_CHARS;
  const canAnalyze = message.trim().length > 0 && !isOverLimit && !loading;

  function handleExampleSelect(e) {
    const id = e.target.value;
    if (!id) return;
    const example = EXAMPLES.find((ex) => ex.id === id);
    if (example) {
      setMessage(example.message);
      textareaRef.current?.focus();
    }
    e.target.value = '';
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey) && canAnalyze) {
      onAnalyze(message);
    }
  }

  return (
    <div>
      <textarea
        ref={textareaRef}
        id="message-input"
        className="message-textarea"
        placeholder="Paste the message you want to analyze..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyDown}
        aria-label="Message to analyze"
        aria-describedby="char-counter"
        disabled={loading}
        rows={8}
      />

      <div className="flex justify-between items-center mt-2">
        <span
          id="char-counter"
          className={`char-count ${isOverLimit ? 'warn' : ''}`}
          aria-live="polite"
        >
          {charCount.toLocaleString()} / {MAX_CHARS.toLocaleString()}
        </span>

        <select
          className="example-select"
          onChange={handleExampleSelect}
          disabled={loading}
          aria-label="Load an example message"
          defaultValue=""
        >
          <option value="" disabled>Load example…</option>
          <optgroup label="Suspicious">
            {EXAMPLES.filter((e) => e.category === 'Suspicious').map((ex) => (
              <option key={ex.id} value={ex.id}>{ex.label}</option>
            ))}
          </optgroup>
          <optgroup label="Benign">
            {EXAMPLES.filter((e) => e.category === 'Benign').map((ex) => (
              <option key={ex.id} value={ex.id}>{ex.label}</option>
            ))}
          </optgroup>
        </select>
      </div>

      <div className="input-actions">
        <button
          id="analyze-btn"
          className="btn btn-primary btn-lg"
          onClick={() => onAnalyze(message)}
          disabled={!canAnalyze}
          aria-label="Analyze message"
        >
          Analyze message
        </button>

        <button
          id="demo-btn"
          className="btn btn-secondary"
          onClick={() => onDemoMode(message || EXAMPLES[0].message)}
          disabled={loading}
          title="Run analysis in demo mode (no API key required)"
        >
          Demo mode
        </button>

        {message && (
          <button
            id="clear-btn"
            className="btn btn-ghost"
            onClick={() => setMessage('')}
            disabled={loading}
            aria-label="Clear message"
          >
            Clear
          </button>
        )}
      </div>

      <p className="text-xs text-subtle mt-2" style={{ marginTop: 'var(--space-3)' }}>
        Ctrl+Enter to analyze
      </p>
    </div>
  );
}
