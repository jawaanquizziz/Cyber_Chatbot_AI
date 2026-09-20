export default function EntityList({ entities }) {
  if (!entities || entities.length === 0) {
    return (
      <div>
        <p className="section-label">Detected entities</p>
        <p className="text-sm text-subtle">No entities extracted.</p>
      </div>
    );
  }

  return (
    <div>
      <p className="section-label">Detected entities</p>
      <div>
        {entities.map((entity, i) => (
          <div className="entity-row" key={i}>
            <span className="entity-type">{entity.type}</span>
            <span className="entity-value">{entity.value}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
