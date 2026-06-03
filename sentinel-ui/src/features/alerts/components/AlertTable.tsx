import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function AlertTable({
  alerts,
  onSelect,
}: {
  alerts: any[];
  onSelect: (alert: any) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Title</TableHead>
          <TableHead>Severity</TableHead>
          <TableHead>Status</TableHead>
          <TableHead>Service</TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {alerts.map((alert) => (
          <TableRow
            key={alert.id}
            className="cursor-pointer"
            onClick={() =>
              onSelect(alert)
            }
          >
            <TableCell>
              {alert.title}
            </TableCell>

            <TableCell>
              {alert.severity}
            </TableCell>

            <TableCell>
              {alert.status}
            </TableCell>

            <TableCell>
              {alert.service}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
