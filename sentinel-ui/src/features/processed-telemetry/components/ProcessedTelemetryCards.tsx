import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export function ProcessedTelemetryCards({
  telemetry,
  onSelect,
}: {
  telemetry: any[];
  onSelect: (
    item: any
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
      {telemetry.map(
        (item) => (
          <Card
            key={item.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                item
              )
            }
          >
            <div
              className="
              flex
              justify-between
              "
            >
              <Badge>
                {
                  item.priority
                }
              </Badge>

              <Badge>
                {
                  item.severity
                }
              </Badge>
            </div>

            <h3
              className="
              mt-3
              font-semibold
              "
            >
              {
                item.service
              }
            </h3>

            <p
              className="
              text-sm
              text-muted-foreground
              "
            >
              {
                item.summary
              }
            </p>

            <div
              className="
              mt-3
              text-sm
              "
            >
              Risk:
              {" "}
              {
                item.risk_score
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}
