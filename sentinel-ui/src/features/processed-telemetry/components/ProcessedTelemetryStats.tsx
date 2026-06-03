import { Card } from "@/components/ui/card";

export function ProcessedTelemetryStats({
  telemetry,
}: {
  telemetry: any[];
}) {

  const critical =
    telemetry.filter(
      (t) =>
        t.severity ===
        "CRITICAL"
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
        Events
        <div className="text-3xl font-bold">
          {telemetry.length}
        </div>
      </Card>

      <Card className="p-4">
        Critical
        <div className="text-3xl font-bold">
          {critical}
        </div>
      </Card>

      <Card className="p-4">
        Services
        <div className="text-3xl font-bold">
          {
            new Set(
              telemetry.map(
                (t) =>
                  t.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Avg Risk
        <div className="text-3xl font-bold">
          {Math.round(
            telemetry.reduce(
              (
                acc,
                item
              ) =>
                acc +
                item.risk_score,
              0
            ) /
              (
                telemetry.length ||
                1
              )
          )}
        </div>
      </Card>
    </div>
  );
}
