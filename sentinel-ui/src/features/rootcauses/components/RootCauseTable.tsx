import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function RootCauseTable({
  rootCauses,
  onSelect,
}: {
  rootCauses: any[];

  onSelect: (
    rootCause: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Priority
          </TableHead>

          <TableHead>
            Service
          </TableHead>

          <TableHead>
            Cause Type
          </TableHead>

          <TableHead>
            Severity
          </TableHead>

          <TableHead>
            Confidence
          </TableHead>

          <TableHead>
            Trigger
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {rootCauses.map(
          (rootCause) => (
            <TableRow
              key={
                rootCause.id
              }
              onClick={() =>
                onSelect(
                  rootCause
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  rootCause
                    .priority
                }
              </TableCell>

              <TableCell>
                {
                  rootCause
                    .service
                }
              </TableCell>

              <TableCell>
                {
                  rootCause
                    .root_cause
                    ?.cause_type
                }
              </TableCell>

              <TableCell>
                {
                  rootCause
                    .severity
                }
              </TableCell>

              <TableCell>
                {Math.round(
                  rootCause.confidence *
                  100
                )}
                %
              </TableCell>

              <TableCell>
                {
                  rootCause
                    .causal_chain
                    ?.trigger
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}