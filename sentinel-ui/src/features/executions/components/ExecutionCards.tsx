import { Card } from "@/components/ui/card";

export function ExecutionCards({
  executions,
  onSelect,
}: {
  executions: any[];

  onSelect: (
    execution: any
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
      {executions.map(
        (execution) => (
          <Card
            key={execution.id}
            onClick={() =>
              onSelect(
                execution
              )
            }
            className="
            p-4
            cursor-pointer
            "
          >
            <h3
              className="
              font-bold
              "
            >
              {
                execution.service
              }
            </h3>

            <div className="mt-2">
              Status:
              {" "}
              {
                execution.status
              }
            </div>

            <div className="mt-2">
              Mode:
              {" "}
              {
                execution.mode
              }
            </div>

            <div className="mt-2">
              Actions:
              {" "}
              {
                execution.actions
                  ?.length
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}