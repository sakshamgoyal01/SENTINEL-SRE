import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function TraceTable({
  traces,
  onSelect,
}: {
  traces: any[];

  onSelect: (
    trace: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Operation
          </TableHead>

          <TableHead>
            Service
          </TableHead>

          <TableHead>
            Latency
          </TableHead>

          <TableHead>
            Status
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {traces.map(
          (trace) => (
            <TableRow
              key={trace.id}
              onClick={() =>
                onSelect(
                  trace
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  trace.operation
                }
              </TableCell>

              <TableCell>
                {
                  trace.service
                }
              </TableCell>

              <TableCell>
                {
                  trace.duration_ms
                }
                ms
              </TableCell>

              <TableCell>
                {
                  trace.status_code
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}