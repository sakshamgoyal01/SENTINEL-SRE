import { Card } from "@/components/ui/card";

export function RemediationStats({
  remediations,
}: {
  remediations: any[];
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
        Total Plans

        <div className="text-3xl font-bold">
          {remediations.length}
        </div>
      </Card>

      <Card className="p-4">
        Runbooks

        <div className="text-3xl font-bold">
          {
            remediations.filter(
              (r) =>
                r.plan?.runbook
            ).length
          }
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              remediations.map(
                (r) =>
                  r.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        High Priority

        <div className="text-3xl font-bold">
          {
            remediations.filter(
              (r) =>
                r.priority ===
                "P1"
            ).length
          }
        </div>
      </Card>
    </div>
  );
}