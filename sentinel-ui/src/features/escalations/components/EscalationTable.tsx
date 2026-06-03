import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function EscalationTable({
  escalations,
  onSelect,
}: {
  escalations: any[];

  onSelect: (
    escalation: any
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
            Team
          </TableHead>

          <TableHead>
            Reason
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {escalations.map(
          (
            escalation
          ) => (
            <TableRow
              key={
                escalation.id
              }
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  escalation
                )
              }
            >
              <TableCell>
                {
                  escalation.service
                }
              </TableCell>

              <TableCell>
                {
                  escalation
                    .target?.team
                }
              </TableCell>

              <TableCell>
                {
                  escalation
                    .escalation_reason
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}