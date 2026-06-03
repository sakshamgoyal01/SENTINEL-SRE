import { Card } from "@/components/ui/card";

export function RiskCards({
  risks,
  onSelect,
}: {
  risks: any[];

  onSelect: (
    risk: any
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
      {risks.map(
        (risk) => (
          <Card
            key={risk.id}
            onClick={() =>
              onSelect(risk)
            }
            className="
            p-4
            cursor-pointer
            hover:border-primary
            transition
            "
          >
            <div
              className="
              text-sm
              font-medium
              "
            >
              {risk.priority}
            </div>

            <h3
              className="
              mt-2
              font-bold
              "
            >
              {risk.service}
            </h3>

            <div
              className="
              mt-4
              space-y-2
              text-sm
              "
            >
              <div>
                Risk Level:
                {" "}
                {
                  risk
                    .risk_summary
                    ?.risk_level
                }
              </div>

              <div>
                Customer Impact:
                {" "}
                {
                  risk
                    .impact_assessment
                    ?.customer_impact
                }
              </div>

              <div>
                Blast Radius:
                {" "}
                {(
                  risk
                    .blast_radius
                    ?.impacted_services ??
                  risk
                    .blast_radius
                    ?.services ??
                  []
                ).length}
              </div>
            </div>
          </Card>
        )
      )}
    </div>
  );
}