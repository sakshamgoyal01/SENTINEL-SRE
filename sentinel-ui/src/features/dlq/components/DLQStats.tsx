import { Card } from "@/components/ui/card";

export function DLQStats({
  entries,
}: {
  entries: any[];
}) {

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Failed Events
        <div className="text-3xl font-bold">
          {entries.length}
        </div>
      </Card>

      <Card className="p-4">
        Topics
        <div className="text-3xl font-bold">
          {
            new Set(
              entries.map(
                (e) =>
                  e.source_topic
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Services
        <div className="text-3xl font-bold">
          {
            new Set(
              entries.map(
                (e) =>
                  e.payload
                    ?.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Errors
        <div className="text-3xl font-bold">
          {entries.length}
        </div>
      </Card>
    </div>
  );
}
