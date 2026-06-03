import { Card } from "@/components/ui/card";

export function RecoveryStats({
  recoveries,
}: {
  recoveries: any[];
}) {

  const completed =
    recoveries.filter(
      (r) =>
        r.recovery_status ===
        "NOT_REQUIRED"
    ).length;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Total

        <div className="text-3xl font-bold">
          {recoveries.length}
        </div>
      </Card>

      <Card className="p-4">
        Completed

        <div className="text-3xl font-bold">
          {completed}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              recoveries.map(
                (r) =>
                  r.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Strategies

        <div className="text-3xl font-bold">
          {
            new Set(
              recoveries.map(
                (r) =>
                  r.strategy
                    ?.type
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}