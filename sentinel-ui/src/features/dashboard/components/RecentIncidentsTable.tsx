import {
  Card,
} from "@/components/ui/card";

import {
  Badge,
} from "@/components/ui/badge";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function RecentIncidentsTable({
  incidents,
}: {
  incidents: any[];
}) {

  return (
    <Card
      className="
      p-6
      "
    >
      <div
        className="
        mb-4
        "
      >
        <h3
          className="
          text-lg
          font-semibold
          "
        >
          Recent Incidents
        </h3>
      </div>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>
              Service
            </TableHead>

            <TableHead>
              Priority
            </TableHead>

            <TableHead>
              Severity
            </TableHead>

            <TableHead>
              Risk
            </TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {incidents
            .slice(0, 5)
            .map(
              (
                incident
              ) => (
                <TableRow
                  key={
                    incident.id
                  }
                >
                  <TableCell>
                    {
                      incident.service
                    }
                  </TableCell>

                  <TableCell>
                    <Badge>
                      {
                        incident.incident_priority
                      }
                    </Badge>
                  </TableCell>

                  <TableCell>
                    <Badge>
                      {
                        incident
                          .aggregated_event
                          ?.severity
                      }
                    </Badge>
                  </TableCell>

                  <TableCell>
                    {
                      incident.final_risk_score
                    }
                  </TableCell>
                </TableRow>
              )
            )}
        </TableBody>
      </Table>
    </Card>
  );
}