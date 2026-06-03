import { Card } from "@/components/ui/card";

export function TraceCards({
  traces,
  onSelect,
}: {
  traces: any[];

  onSelect: (
    trace: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      "
    >
      {traces.map(
        (trace) => (
          <Card
            key={trace.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                trace
              )
            }
          >
            <h3 className="font-bold">
              {
                trace.operation
              }
            </h3>

            <div className="mt-2">
              {
                trace.duration_ms
              }
              ms
            </div>

            <div className="mt-2">
              HTTP
              {" "}
              {
                trace.status_code
              }
            </div>

            <div className="mt-2 text-sm">
              {
                trace.service
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}