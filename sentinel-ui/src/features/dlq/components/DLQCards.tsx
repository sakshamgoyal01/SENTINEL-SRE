import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export function DLQCards({
  entries,
  onSelect,
}: {
  entries: any[];
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
      {entries.map(
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
                DLQ
              </Badge>

              <Badge>
                Failed
              </Badge>
            </div>

            <h3
              className="
              mt-3
              font-semibold
              "
            >
              {
                item.payload
                  ?.service
              }
            </h3>

            <p
              className="
              text-sm
              text-muted-foreground
              "
            >
              {
                item.error_message
              }
            </p>

            <div
              className="
              mt-3
              text-sm
              "
            >
              {
                item.source_topic
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}
