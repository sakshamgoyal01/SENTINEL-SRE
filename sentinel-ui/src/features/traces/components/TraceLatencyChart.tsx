import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

export function TraceLatencyChart({
  traces,
}: {
  traces: any[];
}) {

  const data =
    traces.map(
      (
        trace,
        index
      ) => ({
        name:
          index + 1,

        latency:
          trace.duration_ms,
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
          data={data}
        >
          <XAxis
            dataKey="name"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="latency"
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}