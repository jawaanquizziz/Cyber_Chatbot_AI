import RiskBadge from './RiskBadge';
import IntentCard from './IntentCard';
import EntityList from './EntityList';
import IndicatorList from './IndicatorList';
import RecommendedActions from './RecommendedActions';
import FollowUpChat from './FollowUpChat';

export default function AnalysisSummary({ analysis }) {
  if (!analysis) return null;

  return (
    <div>
      {/* Header */}
      <div className="assessment-section">
        <div className="flex items-center gap-3 mb-2" style={{ flexWrap: 'wrap', gap: 'var(--space-3)' }}>
          <p className="assessment-category">{analysis.category}</p>
          <RiskBadge level={analysis.risk_level} />
          {analysis.is_demo && (
            <span
              style={{
                fontSize: '0.7rem',
                color: 'var(--warn)',
                background: 'var(--warn-dim)',
                border: '1px solid rgba(245,158,11,0.2)',
                borderRadius: 'var(--radius-sm)',
                padding: '2px 8px',
                fontWeight: 600,
                letterSpacing: '0.06em',
                textTransform: 'uppercase',
              }}
            >
              Demo
            </span>
          )}
        </div>
        <p className="assessment-explanation">{analysis.explanation}</p>
      </div>

      <div className="divider" />

      {/* Intent */}
      <div className="assessment-section">
        <IntentCard intent={analysis.intent} explanation={analysis.intent_explanation} />
      </div>

      <div className="divider" />

      {/* Entities */}
      <div className="assessment-section">
        <EntityList entities={analysis.entities} />
      </div>

      <div className="divider" />

      {/* Indicators */}
      <div className="assessment-section">
        <IndicatorList indicators={analysis.indicators} />
      </div>

      <div className="divider" />

      {/* Actions */}
      <div className="assessment-section">
        <RecommendedActions actions={analysis.recommended_actions} />
      </div>

      {/* Follow-up Chat */}
      <FollowUpChat analysis={analysis} />
    </div>
  );
}
