import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

export function MetricChart({
  metrics,
}: {
  metrics: any[];
}) {

  const chartData =
    metrics.map(
      (
        metric,
        index
      ) => ({
        name:
          index + 1,

        value:
          metric.value,
      })
    );

  return (
    <div
      className="
      h-80
      w-full
      "
    >
      <ResponsiveContainer
        width="100%"
        height="100%"
      >
        <LineChart
          data={chartData}
        >
          <XAxis
            dataKey="name"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="value"
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}