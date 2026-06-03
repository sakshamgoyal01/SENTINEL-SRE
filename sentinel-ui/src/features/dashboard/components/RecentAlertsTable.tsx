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

export function RecentAlertsTable({
  alerts,
}: {
  alerts: any[];
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
          Recent Alerts
        </h3>
      </div>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>
              Title
            </TableHead>

            <TableHead>
              Service
            </TableHead>

            <TableHead>
              Severity
            </TableHead>

            <TableHead>
              Status
            </TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {alerts
            .slice(0, 5)
            .map(
              (
                alert
              ) => (
                <TableRow
                  key={
                    alert.id
                  }
                >
                  <TableCell>
                    {
                      alert.title
                    }
                  </TableCell>

                  <TableCell>
                    {
                      alert.service
                    }
                  </TableCell>

                  <TableCell>
                    <Badge>
                      {
                        alert.severity
                      }
                    </Badge>
                  </TableCell>

                  <TableCell>
                    <Badge>
                      {
                        alert.status
                      }
                    </Badge>
                  </TableCell>
                </TableRow>
              )
            )}
        </TableBody>
      </Table>
    </Card>
  );
}