import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function RiskTable({
  risks,
  onSelect,
}: {
  risks: any[];

  onSelect: (
    risk: any
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
            Risk
          </TableHead>

          <TableHead>
            Impact
          </TableHead>

          <TableHead>
            Blast Radius
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {risks.map(
          (risk) => (
            <TableRow
              key={risk.id}
              onClick={() =>
                onSelect(risk)
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {risk.priority}
              </TableCell>

              <TableCell>
                {risk.service}
              </TableCell>

              <TableCell>
                {
                  risk
                    .risk_summary
                    ?.risk_level
                }
              </TableCell>

              <TableCell>
                {
                  risk
                    .impact_assessment
                    ?.customer_impact
                }
              </TableCell>

              <TableCell>
                {(
                  risk
                    .blast_radius
                    ?.impacted_services ??
                  risk
                    .blast_radius
                    ?.services ??
                  []
                ).length}
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}