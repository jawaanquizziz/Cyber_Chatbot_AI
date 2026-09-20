export default function IndicatorList({ indicators }) {
  if (!indicators || indicators.length === 0) {
    return (
      <div>
        <p className="section-label">Why this message was flagged</p>
        <p className="text-sm text-subtle">No significant indicators detected.</p>
      </div>
    );
  }

  return (
    <div>
      <p className="section-label">Why this message was flagged</p>
      {indicators.map((indicator, i) => (
        <div className="indicator-item" key={i}>
          <p className="indicator-name">{indicator.name}</p>
          <p className="indicator-explanation">{indicator.explanation}</p>
        </div>
      ))}
    </div>
  );
}
