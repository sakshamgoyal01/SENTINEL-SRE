import { Card } from "@/components/ui/card";

export function AggregatedEventCards({
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
      xl:grid-cols-3
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
              onSelect(
                event
              )
            }
          >
            <div
              className="
              flex
              justify-between
              "
            >
              <div className="font-bold">
                {
                  event.severity
                }
              </div>

              <div>
                Count:
                {" "}
                {
                  event.count
                }
              </div>
            </div>

            <h3
              className="
              mt-3
              text-lg
              font-semibold
              "
            >
              {
                event.category
              }
            </h3>

            <p className="mt-2">
              {
                event.summary
              }
            </p>
          </Card>
        )
      )}
    </div>
  );
}
