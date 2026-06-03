import { Card } from "@/components/ui/card";

export function StateCards({
  states,
  onSelect,
}: {
  states: any[];
  onSelect: (
    state: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      xl:grid-cols-3
      "
    >
      {states.map(
        (state) => (
          <Card
            key={state.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                state
              )
            }
          >
            <div
              className="
              font-bold
              text-lg
              "
            >
              {
                state.current_state
              }
            </div>

            <div className="mt-2">
              {
                state.service
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              text-muted-foreground
              "
            >
              {
                state.incident_id
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}
