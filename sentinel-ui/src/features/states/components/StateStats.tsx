import { Card } from "@/components/ui/card";

export function StateStats({
  states,
}: {
  states: any[];
}) {

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        States
        <div className="text-3xl font-bold">
          {states.length}
        </div>
      </Card>

      <Card className="p-4">
        Services
        <div className="text-3xl font-bold">
          {
            new Set(
              states.map(
                (s) =>
                  s.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Incidents
        <div className="text-3xl font-bold">
          {
            new Set(
              states.map(
                (s) =>
                  s.incident_id
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Active
        <div className="text-3xl font-bold">
          {states.length}
        </div>
      </Card>
    </div>
  );
}
