import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function ProcessedTelemetryTable({
  telemetry,
  onSelect,
}: {
  telemetry: any[];
  onSelect: (
    item: any
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
            Type
          </TableHead>

          <TableHead>
            Severity
          </TableHead>

          <TableHead>
            Risk
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {telemetry.map(
          (item) => (
            <TableRow
              key={item.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  item
                )
              }
            >
              <TableCell>
                {item.service}
              </TableCell>

              <TableCell>
                {
                  item.event_type
                }
              </TableCell>

              <TableCell>
                {
                  item.severity
                }
              </TableCell>

              <TableCell>
                {
                  item.risk_score
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
