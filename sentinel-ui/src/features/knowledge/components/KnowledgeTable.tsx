import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function KnowledgeTable({
  entries,
  onSelect,
}: {
  entries: any[];
  onSelect: (
    entry: any
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
            Incident Type
          </TableHead>

          <TableHead>
            Success
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {entries.map(
          (entry) => (
            <TableRow
              key={entry.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  entry
                )
              }
            >
              <TableCell>
                {entry.service}
              </TableCell>

              <TableCell>
                {
                  entry.pattern
                    ?.incident_type
                }
              </TableCell>

              <TableCell>
                {entry.remediation
                  ?.successful
                  ? "Yes"
                  : "No"}
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
