import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function RecoveryTable({
  recoveries,
  onSelect,
}: {
  recoveries: any[];

  onSelect: (
    recovery: any
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
            Strategy
          </TableHead>

          <TableHead>
            Verification
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {recoveries.map(
          (recovery) => (
            <TableRow
              key={recovery.id}
              onClick={() =>
                onSelect(
                  recovery
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  recovery.service
                }
              </TableCell>

              <TableCell>
                {
                  recovery
                    .recovery_status
                }
              </TableCell>

              <TableCell>
                {
                  recovery
                    .strategy
                    ?.type
                }
              </TableCell>

              <TableCell>
                {
                  recovery
                    .verification_id
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}