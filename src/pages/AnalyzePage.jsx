import MessageInput from '../components/MessageInput';
import AnalysisSummary from '../components/AnalysisSummary';
import EmptyState from '../components/EmptyState';
import LoadingState from '../components/LoadingState';
import ErrorState from '../components/ErrorState';
import { useAnalysis } from '../hooks/useAnalysis';

export default function AnalyzePage() {
  const {
    analysis,
    loading,
    loadingStep,
    loadingSteps,
    error,
    currentMessage,
    run,
  } = useAnalysis();

  function handleDemoMode(message) {
    run(message, true);
  }

  function handleRetry() {
    if (currentMessage) run(currentMessage, false);
  }

  return (
    <main className="page-content">
      <div className="analyze-header">
        <h1 className="analyze-title">Analyze a message</h1>
        <p className="analyze-subtitle">
          Understand suspicious signals before taking action.
        </p>
      </div>

      <div className="analyze-grid">
        {/* Left: Input */}
        <section aria-label="Message input">
          <MessageInput
            onAnalyze={(msg) => run(msg, false)}
            onDemoMode={handleDemoMode}
            loading={loading}
          />

          <p
            className="disclaimer"
            style={{ marginTop: 'var(--space-4)' }}
            role="note"
          >
            <span aria-hidden="true" style={{ color: 'var(--text-subtle)' }}>ⓘ</span>
            AI-assisted assessment. Verify important messages through trusted
            official channels.
          </p>
        </section>

        {/* Right: Assessment panel */}
        <section className="assessment-panel" aria-label="Assessment">
          <div className="assessment-header">
            <span className="assessment-header-title">Assessment</span>
            {analysis && (
              <span className="text-xs text-subtle">
                {analysis.is_demo ? 'Demo result' : 'Live analysis'}
              </span>
            )}
          </div>

          <div className="assessment-body">
            {loading && (
              <LoadingState steps={loadingSteps} currentStep={loadingStep} />
            )}
            {!loading && error && (
              <ErrorState
                message={error}
                onRetry={handleRetry}
                onDemoMode={() => handleDemoMode(currentMessage || '')}
              />
            )}
            {!loading && !error && !analysis && <EmptyState />}
            {!loading && !error && analysis && (
              <AnalysisSummary analysis={analysis} />
            )}
          </div>
        </section>
      </div>
    </main>
  );
}
