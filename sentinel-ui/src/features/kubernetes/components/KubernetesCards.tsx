import { Card } from "@/components/ui/card";

export function KubernetesCards({
  events,
  onSelect,
}: {
  events: any[];

  onSelect: (
    event: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      "
    >
      {events.map(
        (event) => (
          <Card
            key={event.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(event)
            }
          >
            <div
              className="
              font-bold
              "
            >
              {
                event.reason
              }
            </div>

            <div className="mt-2">
              {
                event.message
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              "
            >
              {
                event
                  .involved_object
                  ?.name
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}