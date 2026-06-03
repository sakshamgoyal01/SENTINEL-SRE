import { Card } from "@/components/ui/card";

export function TraceStats({
  traces,
}: {
  traces: any[];
}) {

  const avgLatency =
    traces.length
      ? (
          traces.reduce(
            (
              total,
              trace
            ) =>
              total +
              trace.duration_ms,
            0
          ) /
          traces.length
        ).toFixed(1)
      : 0;

  const failures =
    traces.filter(
      (trace) =>
        trace.status_code >=
        500
    ).length;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Total Traces

        <div className="text-3xl font-bold">
          {traces.length}
        </div>
      </Card>

      <Card className="p-4">
        Avg Latency

        <div className="text-3xl font-bold">
          {avgLatency}
          ms
        </div>
      </Card>

      <Card className="p-4">
        Failures

        <div className="text-3xl font-bold">
          {failures}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              traces.map(
                (t) =>
                  t.service
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}