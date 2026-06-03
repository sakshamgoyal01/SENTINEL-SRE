import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function DLQTable({
  entries,
  onSelect,
}: {
  entries: any[];
  onSelect: (
    item: any
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
            Topic
          </TableHead>

          <TableHead>
            Error
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {entries.map(
          (item) => (
            <TableRow
              key={item.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  item
                )
              }
            >
              <TableCell>
                {
                  item.payload
                    ?.service
                }
              </TableCell>

              <TableCell>
                {
                  item.source_topic
                }
              </TableCell>

              <TableCell>
                {
                  item.error_message
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
