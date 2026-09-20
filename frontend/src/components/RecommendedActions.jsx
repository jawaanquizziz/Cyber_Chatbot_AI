export default function RecommendedActions({ actions }) {
  if (!actions || actions.length === 0) return null;

  return (
    <div>
      <p className="section-label">Recommended next steps</p>
      <ol className="action-list">
        {actions.map((action, i) => (
          <li className="action-item" key={i}>
            <span className="text-sm">{action}</span>
          </li>
        ))}
      </ol>
    </div>
  );
}
