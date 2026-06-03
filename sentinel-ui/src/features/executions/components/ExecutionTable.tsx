import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function ExecutionTable({
  executions,
  onSelect,
}: {
  executions: any[];

  onSelect: (
    execution: any
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
            Status
          </TableHead>

          <TableHead>
            Executed
          </TableHead>

          <TableHead>
            Mode
          </TableHead>

          <TableHead>
            Actions
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {executions.map(
          (execution) => (
            <TableRow
              key={
                execution.id
              }
              onClick={() =>
                onSelect(
                  execution
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  execution.service
                }
              </TableCell>

              <TableCell>
                {
                  execution.status
                }
              </TableCell>

              <TableCell>
                {execution.executed
                  ? "YES"
                  : "NO"}
              </TableCell>

              <TableCell>
                {
                  execution.mode
                }
              </TableCell>

              <TableCell>
                {
                  execution.actions
                    ?.length
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}