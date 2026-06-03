import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
}
from "@/components/ui/table";

export function InvestigationTable({
  investigations,
  onSelect,
}: {
  investigations: any[];

  onSelect: (
    investigation: any
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
            Confidence
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {investigations.map(
          (
            investigation
          ) => (
            <TableRow
              key={
                investigation.id
              }
              onClick={() =>
                onSelect(
                  investigation
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  investigation.priority
                }
              </TableCell>

              <TableCell>
                {
                  investigation.service
                }
              </TableCell>

              <TableCell>
                {
                  investigation.severity
                }
              </TableCell>

              <TableCell>
                {Math.round(
                  investigation.confidence *
                  100
                )}
                %
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}