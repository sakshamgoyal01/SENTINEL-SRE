import {
  Card,
} from "@/components/ui/card";

import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Tooltip,
  Cell,
} from "recharts";

export function RiskDistributionChart({
  risks,
}: {
  risks: any[];
}) {

  const grouped = {
    CRITICAL: 0,
    HIGH: 0,
    MEDIUM: 0,
    LOW: 0,
  };

  risks.forEach(
    (risk) => {

      const level =
        risk
          .risk_summary
          ?.risk_level;

      if (
        grouped[
          level as keyof typeof grouped
        ] !== undefined
      ) {
        grouped[
          level as keyof typeof grouped
        ]++;
      }
    }
  );

  const data = [
    {
      name:
        "Critical",
      value:
        grouped.CRITICAL,
    },

    {
      name: "High",
      value:
        grouped.HIGH,
    },

    {
      name:
        "Medium",
      value:
        grouped.MEDIUM,
    },

    {
      name: "Low",
      value:
        grouped.LOW,
    },
  ];

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
          Risk Distribution
        </h3>

        <p
          className="
          text-sm
          text-muted-foreground
          "
        >
          Current risk posture
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
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              outerRadius={
                120
              }
            >
              <Cell />
              <Cell />
              <Cell />
              <Cell />
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}