export default function ErrorState({ message, onRetry, onDemoMode }) {
  return (
    <div className="error-state" role="alert">
      <p className="error-title">Analysis could not be completed</p>
      <p className="error-message">
        {message || 'An unexpected error occurred. Check that the backend server is running.'}
      </p>
      <div className="error-actions">
        {onRetry && (
          <button className="btn btn-secondary btn-sm" onClick={onRetry} id="retry-btn">
            Try again
          </button>
        )}
        {onDemoMode && (
          <button className="btn btn-ghost btn-sm" onClick={onDemoMode} id="use-demo-btn">
            Use demo mode
          </button>
        )}
      </div>
    </div>
  );
}
