import { Card } from "@/components/ui/card";

export function RootCauseStats({
  rootCauses,
}: {
  rootCauses: any[];
}) {
  const critical =
    rootCauses.filter(
      (r) =>
        r.severity ===
        "CRITICAL"
    ).length;

  const avgConfidence =
    rootCauses.length > 0
      ? (
          rootCauses.reduce(
            (
              sum,
              r
            ) =>
              sum +
              r.confidence,
            0
          ) /
          rootCauses.length
        ).toFixed(2)
      : "0";

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Root Causes

        <div className="text-3xl font-bold">
          {rootCauses.length}
        </div>
      </Card>

      <Card className="p-4">
        Critical

        <div className="text-3xl font-bold">
          {critical}
        </div>
      </Card>

      <Card className="p-4">
        Avg Confidence

        <div className="text-3xl font-bold">
          {avgConfidence}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              rootCauses.map(
                (r) =>
                  r.service
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}