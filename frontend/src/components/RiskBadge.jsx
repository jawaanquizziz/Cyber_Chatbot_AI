export default function RiskBadge({ level }) {
  if (!level) return null;
  const labels = { HIGH: 'High Risk', MEDIUM: 'Medium Risk', LOW: 'Low Risk' };
  return (
    <span className={`risk-badge ${level}`} aria-label={`Risk level: ${labels[level] || level}`}>
      {level}
    </span>
  );
}
