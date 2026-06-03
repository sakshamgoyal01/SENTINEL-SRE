import { Card }
from "@/components/ui/card";

export function RiskStats({
  risks,
}: {
  risks: any[];
}) {

  const critical =
    risks.filter(
      (r) =>
        r.risk_summary
          ?.risk_level ===
        "CRITICAL"
    ).length;

  const highImpact =
    risks.filter(
      (r) =>
        r.impact_assessment
          ?.customer_impact ===
        "HIGH"
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
        Total Risks

        <div className="text-3xl font-bold">
          {risks.length}
        </div>
      </Card>

      <Card className="p-4">
        Critical

        <div className="text-3xl font-bold">
          {critical}
        </div>
      </Card>

      <Card className="p-4">
        High Impact

        <div className="text-3xl font-bold">
          {highImpact}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              risks.map(
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