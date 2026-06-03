import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function RemediationTable({
  remediations,
  onSelect,
}: {
  remediations: any[];

  onSelect: (
    remediation: any
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
            Runbook
          </TableHead>

          <TableHead>
            Risk ID
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {remediations.map(
          (remediation) => (
            <TableRow
              key={
                remediation.id
              }
              onClick={() =>
                onSelect(
                  remediation
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  remediation.priority
                }
              </TableCell>

              <TableCell>
                {
                  remediation.service
                }
              </TableCell>

              <TableCell>
                {
                  remediation
                    .plan
                    ?.runbook
                }
              </TableCell>

              <TableCell>
                {
                  remediation
                    .risk_id
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}