import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function AuditTable({
  audits,
  onSelect,
}: {
  audits: any[];

  onSelect: (
    audit: any
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
            Details
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {audits.map(
          (audit) => (
            <TableRow
              key={audit.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  audit
                )
              }
            >
              <TableCell>
                {
                  audit.service
                }
              </TableCell>

              <TableCell>
                {
                  audit.status
                }
              </TableCell>

              <TableCell>
                {
                  audit.details
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}