import { Card } from "@/components/ui/card";

export function RecoveryCards({
  recoveries,
  onSelect,
}: {
  recoveries: any[];

  onSelect: (
    recovery: any
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
      {recoveries.map(
        (recovery) => (
          <Card
            key={recovery.id}
            onClick={() =>
              onSelect(
                recovery
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
                recovery.service
              }
            </h3>

            <div className="mt-2">
              Status:
              {" "}
              {
                recovery
                  .recovery_status
              }
            </div>

            <div className="mt-2">
              Strategy:
              {" "}
              {
                recovery
                  .strategy
                  ?.type
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}