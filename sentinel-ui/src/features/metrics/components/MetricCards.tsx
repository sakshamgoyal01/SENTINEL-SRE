import { Card } from "@/components/ui/card";

export function MetricCards({
  metrics,
  onSelect,
}: {
  metrics: any[];

  onSelect: (
    metric: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      xl:grid-cols-3
      "
    >
      {metrics.map(
        (metric) => (
          <Card
            key={metric.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(metric)
            }
          >
            <h3
              className="
              font-bold
              "
            >
              {
                metric.metric_name
              }
            </h3>

            <div
              className="
              text-3xl
              font-bold
              mt-3
              "
            >
              {metric.value}
              {" "}
              {
                metric.unit
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              text-muted-foreground
              "
            >
              {
                metric.service
              }
            </div>

            <div
              className="
              mt-2
              text-xs
              "
            >
              Pod:
              {" "}
              {
                metric.labels
                  ?.pod
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}