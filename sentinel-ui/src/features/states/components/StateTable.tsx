import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function StateTable({
  states,
  onSelect,
}: {
  states: any[];
  onSelect: (
    state: any
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
            State
          </TableHead>

          <TableHead>
            Incident
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {states.map(
          (state) => (
            <TableRow
              key={state.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  state
                )
              }
            >
              <TableCell>
                {state.service}
              </TableCell>

              <TableCell>
                {
                  state.current_state
                }
              </TableCell>

              <TableCell>
                {
                  state.incident_id
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}
