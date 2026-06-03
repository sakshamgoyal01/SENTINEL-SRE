import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import { SeverityBadge }
  from "./SeverityBadge";

export function IncidentTable({
  incidents,
  onSelect,
}: {
  incidents: any[];
  onSelect: (
    incident: any
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
            Severity
          </TableHead>

          <TableHead>
            Risk
          </TableHead>

          <TableHead>
            Impact
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {incidents.map(
          (incident) => (
            <TableRow
              key={incident.id}
              onClick={() =>
                onSelect(
                  incident
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  incident
                    .incident_priority
                }
              </TableCell>

              <TableCell>
                {
                  incident
                    .service
                }
              </TableCell>

              <TableCell>
                <SeverityBadge
                  severity={
                    incident
                      .aggregated_event
                      ?.severity
                  }
                />
              </TableCell>

              <TableCell>
                {
                  incident
                    .final_risk_score
                }
              </TableCell>

              <TableCell>
                {
                  incident
                    .impact_score
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}