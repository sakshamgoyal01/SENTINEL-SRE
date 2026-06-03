import { Card } from "@/components/ui/card";

export function KnowledgeStats({
  entries,
}: {
  entries: any[];
}) {

  const successful =
    entries.filter(
      (entry) =>
        entry.remediation
          ?.successful
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
        Patterns
        <div className="text-3xl font-bold">
          {entries.length}
        </div>
      </Card>

      <Card className="p-4">
        Successful
        <div className="text-3xl font-bold">
          {successful}
        </div>
      </Card>

      <Card className="p-4">
        Services
        <div className="text-3xl font-bold">
          {
            new Set(
              entries.map(
                (e) =>
                  e.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Incident Types
        <div className="text-3xl font-bold">
          {
            new Set(
              entries.map(
                (e) =>
                  e.pattern
                    ?.incident_type
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}
