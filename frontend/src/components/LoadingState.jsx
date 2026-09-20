export default function LoadingState({ steps, currentStep }) {
  return (
    <div className="loading-steps" role="status" aria-label="Analyzing message">
      <p className="section-label" style={{ marginBottom: 'var(--space-4)' }}>
        Analyzing message
      </p>
      {steps.map((step, i) => {
        const isDone = i < currentStep;
        const isActive = i === currentStep;
        return (
          <div
            key={step}
            className={`loading-step ${isDone ? 'done' : isActive ? 'active' : ''}`}
          >
            <span className="loading-spinner" aria-hidden="true" />
            {step}
          </div>
        );
      })}
    </div>
  );
}
