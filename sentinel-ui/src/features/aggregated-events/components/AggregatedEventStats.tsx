import { Card } from "@/components/ui/card";

export function AggregatedEventStats({
  events,
}: {
  events: any[];
}) {

  const totalCount =
    events.reduce(
      (
        sum,
        event
      ) =>
        sum +
        event.count,
      0
    );

  const critical =
    events.filter(
      (event) =>
        event.severity ===
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
          {events.length}
        </div>
      </Card>

      <Card className="p-4">
        Total Count

        <div className="text-3xl font-bold">
          {totalCount}
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
              events.flatMap(
                (
                  event
                ) =>
                  event.services
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}
