import { Card } from "@/components/ui/card";

export function ReportStats({
  reports,
}: {
  reports: any[];
}) {

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-3
      "
    >
      <Card className="p-4">
        Reports

        <div className="text-3xl font-bold">
          {reports.length}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              reports.map(
                (r) =>
                  r.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Generated

        <div className="text-3xl font-bold">
          {reports.length}
        </div>
      </Card>
    </div>
  );
}
