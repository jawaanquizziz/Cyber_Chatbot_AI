const NLP_CONCEPTS = [
  {
    concept: 'Natural Language Understanding',
    implementation: 'Understands message meaning, tone, and security context to produce a category and risk assessment.',
  },
  {
    concept: 'Intent Detection',
    implementation: 'Identifies the likely purpose of the message — credential theft, payment fraud, malware delivery, or informational.',
  },
  {
    concept: 'Entity Extraction',
    implementation: 'Extracts URLs, organizations, email addresses, monetary values, OTP references, and requested information from message text.',
  },
  {
    concept: 'Contextual Interaction',
    implementation: 'Follow-up questions are answered using the current analysis as context, enabling multi-turn dialogue about the same message.',
  },
  {
    concept: 'Information Retrieval',
    implementation: 'A local cybersecurity knowledge base provides category definitions and indicator patterns to inform analysis.',
  },
  {
    concept: 'AI Response Generation',
    implementation: 'The AI produces a structured explanation and a set of recommended actions tailored to the specific message content.',
  },
  {
    concept: 'Task-oriented Dialogue',
    implementation: 'The system guides users toward safe, specific next steps rather than providing generic advice.',
  },
];

export default function AboutPage() {
  return (
    <main className="page-content">
      <div style={{ maxWidth: '720px' }}>
        <div className="analyze-header">
          <h1 className="analyze-title">About CyberGuard</h1>
        </div>

        <div className="card" style={{ marginBottom: 'var(--space-6)' }}>
          <p className="text-sm" style={{ lineHeight: 1.7, color: 'var(--text-muted)' }}>
            CyberGuard is an academic prototype demonstrating how Natural Language
            Processing and conversational AI can support cybersecurity awareness.
            It analyzes suspicious messages and presents a structured security
            assessment — identifying intent, extracting entities, explaining
            flagged signals, and suggesting safe responses.
          </p>
        </div>

        <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--space-4)', color: 'var(--text)' }}>
          NLP techniques demonstrated
        </h2>

        <table className="about-table">
          <thead>
            <tr>
              <th scope="col">NLP Concept</th>
              <th scope="col">CyberGuard Implementation</th>
            </tr>
          </thead>
          <tbody>
            {NLP_CONCEPTS.map((row) => (
              <tr key={row.concept}>
                <td>{row.concept}</td>
                <td>{row.implementation}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--space-4)', color: 'var(--text)' }}>
          Architecture
        </h2>

        <div
          className="card"
          style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem', color: 'var(--text-muted)', lineHeight: 2.2, marginBottom: 'var(--space-6)' }}
        >
          {[
            'React (Vite)',
            '↓',
            'FastAPI Backend',
            '↓',
            'Deterministic NLP Engine (regex)',
            '↓',
            'Ollama — Llama 3.2 3B (local LLM)',
            '↓',
            'Validated JSON Response',
            '↓',
            'React (Vite)',
          ].map((step, i) => (
            <div key={i} style={{ color: step === '↓' ? 'var(--text-subtle)' : 'var(--text-muted)', paddingLeft: step === '↓' ? 'var(--space-4)' : '0' }}>
              {step}
            </div>
          ))}
        </div>

        <h2 style={{ fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--space-4)', color: 'var(--text)' }}>
          Limitations
        </h2>

        <div className="card card-sm" style={{ marginBottom: 'var(--space-4)', borderLeft: '3px solid var(--border-hover)' }}>
          <p className="text-sm" style={{ color: 'var(--text-muted)', lineHeight: 1.7 }}>
            CyberGuard provides an AI-assisted assessment and should not be treated as
            definitive proof that a message is malicious or safe. The system may
            produce false positives on legitimate urgent messages and may not detect
            sophisticated, novel phishing attempts. Always verify through trusted
            official channels.
          </p>
        </div>

        <div
          className="card card-sm"
          style={{ color: 'var(--text-muted)', fontSize: '0.8125rem', lineHeight: 1.6 }}
        >
          <p style={{ marginBottom: 'var(--space-2)' }}>
            <strong style={{ color: 'var(--text)' }}>Tech stack</strong>
          </p>
          <p>Frontend: React 18, Vite, React Router v7, Vanilla CSS</p>
          <p>Backend: Python 3.10+, FastAPI, Pydantic v2, Uvicorn</p>
          <p>AI Model: Llama 3.2 3B — 3.21B params, 128K context, Q4_K_M quantized</p>
          <p>Inference: Ollama (local, fully offline — no data sent to cloud)</p>
          <p>NLP: Deterministic regex engine + Llama 3.2 structured generation</p>
        </div>
      </div>
    </main>
  );
}
