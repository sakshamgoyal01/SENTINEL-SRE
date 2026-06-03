import { Card } from "@/components/ui/card";

export function AlertCards({
  alerts,
  onSelect,
}: {
  alerts: any[];
  onSelect: (alert: any) => void;
}) {
  return (
    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      {alerts.map((alert) => (
        <Card
          key={alert.id}
          className="p-4 cursor-pointer"
          onClick={() =>
            onSelect(alert)
          }
        >
          <div className="flex justify-between">
            <div className="font-bold">
              {alert.severity}
            </div>

            <div>
              {alert.status}
            </div>
          </div>

          <h3 className="mt-3 text-lg font-semibold">
            {alert.title}
          </h3>

          <p className="mt-2 text-sm">
            {alert.description}
          </p>

          <div className="mt-2 text-sm text-muted-foreground">
            {alert.service}
          </div>
        </Card>
      ))}
    </div>
  );
}
