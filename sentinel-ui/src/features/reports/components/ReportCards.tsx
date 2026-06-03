import { Card } from "@/components/ui/card";

export function ReportCards({
  reports,
  onSelect,
}: {
  reports: any[];

  onSelect: (
    report: any
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
      {reports.map(
        (report) => (
          <Card
            key={report.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                report
              )
            }
          >
            <div
              className="
              font-semibold
              "
            >
              {report.service}
            </div>

            <div
              className="
              mt-2
              text-sm
              "
            >
              {
                report.summary
                  ?.incident_summary
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}
