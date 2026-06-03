import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

export function IncidentTrendChart({
  incidents,
}: {
  incidents: any[];
}) {
  const data =
    incidents.map(
      (incident) => ({
        id:
          incident.id.slice(
            0,
            6
          ),

        risk:
          incident.final_risk_score,
      })
    );

  return (
    <div
      className="
      h-80
      "
    >
      <ResponsiveContainer
        width="100%"
        height="100%"
      >
        <AreaChart data={data}>
          <XAxis
            dataKey="id"
          />

          <YAxis />

          <Tooltip />

          <Area
            dataKey="risk"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}