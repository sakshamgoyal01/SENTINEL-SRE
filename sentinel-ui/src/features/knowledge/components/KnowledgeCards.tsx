import { Card } from "@/components/ui/card";

export function KnowledgeCards({
  entries,
  onSelect,
}: {
  entries: any[];
  onSelect: (
    entry: any
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
        (entry) => (
          <Card
            key={entry.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                entry
              )
            }
          >
            <div className="font-bold">
              {
                entry.pattern
                  ?.incident_type
              }
            </div>

            <div className="mt-2">
              Service:
              {" "}
              {entry.service}
            </div>

            <div className="mt-2">
              Remediation:
              {" "}
              {entry.remediation
                ?.successful
                ? "Successful"
                : "Failed"}
            </div>
          </Card>
        )
      )}
    </div>
  );
}
