import { Card } from "@/components/ui/card";

export function EscalationStats({
  escalations,
}: {
  escalations: any[];
}) {

  const teams =
    new Set(
      escalations.map(
        (e) =>
          e.target?.team
      )
    ).size;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-3
      "
    >
      <Card className="p-4">
        Escalations

        <div className="text-3xl font-bold">
          {escalations.length}
        </div>
      </Card>

      <Card className="p-4">
        Teams

        <div className="text-3xl font-bold">
          {teams}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              escalations.map(
                (e) =>
                  e.service
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}