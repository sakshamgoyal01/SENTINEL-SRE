import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function KubernetesTable({
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
            Type
          </TableHead>

          <TableHead>
            Reason
          </TableHead>

          <TableHead>
            Object
          </TableHead>

          <TableHead>
            Message
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {events.map(
          (event) => (
            <TableRow
              key={event.id}
              onClick={() =>
                onSelect(event)
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  event.event_type
                }
              </TableCell>

              <TableCell>
                {
                  event.reason
                }
              </TableCell>

              <TableCell>
                {
                  event
                    .involved_object
                    ?.name
                }
              </TableCell>

              <TableCell>
                {
                  event.message
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}