import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function ApprovalTable({
  approvals,
  onSelect,
}: {
  approvals: any[];

  onSelect: (
    approval: any
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
            Approved
          </TableHead>

          <TableHead>
            Human Review
          </TableHead>

          <TableHead>
            Actions
          </TableHead>

          <TableHead>
            Reason
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {approvals.map(
          (approval) => (
            <TableRow
              key={approval.id}
              onClick={() =>
                onSelect(
                  approval
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  approval.service
                }
              </TableCell>

              <TableCell>
                {approval.approved
                  ? "YES"
                  : "NO"}
              </TableCell>

              <TableCell>
                {approval.requires_human_approval
                  ? "YES"
                  : "NO"}
              </TableCell>

              <TableCell>
                {
                  approval.actions
                    ?.length
                }
              </TableCell>

              <TableCell>
                {
                  approval.reason
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}