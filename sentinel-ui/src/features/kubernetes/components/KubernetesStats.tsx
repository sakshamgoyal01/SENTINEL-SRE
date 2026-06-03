import { Card } from "@/components/ui/card";

export function KubernetesStats({
  events,
}: {
  events: any[];
}) {

  const warnings =
    events.filter(
      (event) =>
        event.event_type ===
        "Warning"
    ).length;

  const pods =
    new Set(
      events.map(
        (event) =>
          event
            .involved_object
            ?.name
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
        Events

        <div className="text-3xl font-bold">
          {events.length}
        </div>
      </Card>

      <Card className="p-4">
        Warnings

        <div className="text-3xl font-bold">
          {warnings}
        </div>
      </Card>

      <Card className="p-4">
        Pods

        <div className="text-3xl font-bold">
          {pods}
        </div>
      </Card>

      <Card className="p-4">
        Reasons

        <div className="text-3xl font-bold">
          {
            new Set(
              events.map(
                (e) =>
                  e.reason
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}