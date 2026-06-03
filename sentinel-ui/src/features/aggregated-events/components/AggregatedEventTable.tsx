import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function AggregatedEventTable({
  events,
  onSelect,
}: {
  events: any[];
  onSelect: (
    event: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Category
          </TableHead>

          <TableHead>
            Severity
          </TableHead>

          <TableHead>
            Count
          </TableHead>

          <TableHead>
            Services
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {events.map(
          (event) => (
            <TableRow
              key={event.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  event
                )
              }
            >
              <TableCell>
                {
                  event.category
                }
              </TableCell>

              <TableCell>
                {
                  event.severity
                }
              </TableCell>

              <TableCell>
                {
                  event.count
                }
              </TableCell>

              <TableCell>
                {
                  event.services.join(
                    ", "
                  )
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
