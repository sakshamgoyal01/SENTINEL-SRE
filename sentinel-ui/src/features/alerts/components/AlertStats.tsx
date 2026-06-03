import { Card } from "@/components/ui/card";

export function AlertStats({
  alerts,
}: {
  alerts: any[];
}) {
  const critical =
    alerts.filter(
      (a) => a.severity === "CRITICAL"
    ).length;

  const open =
    alerts.filter(
      (a) => a.status === "OPEN"
    ).length;

  return (
    <div className="grid gap-4 md:grid-cols-4">
      <Card className="p-4">
        Alerts
        <div className="text-3xl font-bold">
          {alerts.length}
        </div>
      </Card>

      <Card className="p-4">
        Critical
        <div className="text-3xl font-bold">
          {critical}
        </div>
      </Card>

      <Card className="p-4">
        Open
        <div className="text-3xl font-bold">
          {open}
        </div>
      </Card>

      <Card className="p-4">
        Services
        <div className="text-3xl font-bold">
          {
            new Set(
              alerts.map(
                (a) => a.service
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}
