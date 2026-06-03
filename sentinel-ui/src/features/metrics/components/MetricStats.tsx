import { Card } from "@/components/ui/card";

export function MetricStats({
  metrics,
}: {
  metrics: any[];
}) {

  const avg =
    metrics.length
      ? (
          metrics.reduce(
            (
              total,
              metric
            ) =>
              total +
              metric.value,
            0
          ) /
          metrics.length
        ).toFixed(1)
      : 0;

  const max =
    metrics.length
      ? Math.max(
          ...metrics.map(
            (m) =>
              m.value
          )
        )
      : 0;

  const services =
    new Set(
      metrics.map(
        (m) =>
          m.service
      )
    ).size;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Total Metrics

        <div className="text-3xl font-bold">
          {metrics.length}
        </div>
      </Card>

      <Card className="p-4">
        Average

        <div className="text-3xl font-bold">
          {avg}
        </div>
      </Card>

      <Card className="p-4">
        Max Value

        <div className="text-3xl font-bold">
          {max}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {services}
        </div>
      </Card>
    </div>
  );
}