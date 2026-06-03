import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function ReportTable({
  reports,
  onSelect,
}: {
  reports: any[];

  onSelect: (
    report: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Service
          </TableHead>

          <TableHead>
            Summary
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {reports.map(
          (report) => (
            <TableRow
              key={report.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  report
                )
              }
            >
              <TableCell>
                {
                  report.service
                }
              </TableCell>

              <TableCell>
                {
                  report.summary
                    ?.incident_summary
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
