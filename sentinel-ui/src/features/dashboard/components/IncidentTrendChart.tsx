import {
  Card,
} from "@/components/ui/card";

import {
  ResponsiveContainer,
  AreaChart,
  Area,
  CartesianGrid,
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
      (
        incident,
        index
      ) => ({
        name:
          `#${index + 1}`,

        risk:
          incident.final_risk_score ??
          0,
      })
    );

  return (
    <Card
      className="
      p-6
      "
    >
      <div
        className="
        mb-4
        "
      >
        <h3
          className="
          text-lg
          font-semibold
          "
        >
          Incident Risk Trend
        </h3>

        <p
          className="
          text-sm
          text-muted-foreground
          "
        >
          Risk score evolution
        </p>
      </div>

      <div
        className="
        h-[320px]
        "
      >
        <ResponsiveContainer
          width="100%"
          height="100%"
        >
          <AreaChart
            data={data}
          >
            <CartesianGrid
              strokeDasharray="3 3"
            />

            <XAxis
              dataKey="name"
            />

            <YAxis />

            <Tooltip />

            <Area
              type="monotone"
              dataKey="risk"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}