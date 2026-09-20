import { useState, useRef, useEffect } from 'react';
import { sendChatMessage } from '../services/api';

const SUGGESTED_QUESTIONS = [
  'Why was this flagged?',
  'What information is the sender trying to obtain?',
  'What should I do next?',
  'Which part of the message is suspicious?',
  'How can I verify this safely?',
];

export default function FollowUpChat({ analysis }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const scrollRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  async function sendMessage(text) {
    if (!text.trim() || loading) return;

    const userMsg = { role: 'user', content: text.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await sendChatMessage(text.trim(), analysis);
      setMessages((prev) => [...prev, { role: 'assistant', content: res.answer }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content:
            'Unable to process your question. Please check that the backend is running.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(input);
    }
  }

  return (
    <section aria-label="Follow-up questions">
      <div className="divider" />
      <div style={{ marginBottom: 'var(--space-4)' }}>
        <p className="section-label">Ask about this assessment</p>
        <p className="text-xs text-muted">
          Ask CyberGuard why something was flagged or what you should do next.
        </p>
      </div>

      {messages.length === 0 && (
        <div className="suggested-questions" role="list" aria-label="Suggested questions">
          {SUGGESTED_QUESTIONS.map((q) => (
            <button
              key={q}
              className="suggested-q"
              onClick={() => sendMessage(q)}
              disabled={loading}
              role="listitem"
            >
              {q}
            </button>
          ))}
        </div>
      )}

      {messages.length > 0 && (
        <div className="chat-messages" ref={scrollRef} aria-live="polite">
          {messages.map((msg, i) => (
            <div key={i} className={`chat-bubble ${msg.role}`}>
              {msg.content}
            </div>
          ))}
          {loading && (
            <div className="chat-bubble loading">Analyzing your question…</div>
          )}
        </div>
      )}

      <div className="chat-input-row">
        <input
          id="chat-input"
          className="chat-input"
          type="text"
          placeholder="Ask a follow-up question…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
          aria-label="Follow-up question"
        />
        <button
          id="chat-send-btn"
          className="btn btn-secondary btn-sm"
          onClick={() => sendMessage(input)}
          disabled={!input.trim() || loading}
          aria-label="Send question"
        >
          Send
        </button>
      </div>
    </section>
  );
}
