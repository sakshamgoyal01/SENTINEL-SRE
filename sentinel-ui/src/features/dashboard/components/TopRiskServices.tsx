import {
  Card,
} from "@/components/ui/card";

import {
  Badge,
} from "@/components/ui/badge";

export function TopRiskServices({
  risks,
}: {
  risks: any[];
}) {

  return (
    <Card
      className="
      p-6
      "
    >
      <div
        className="
        mb-4
        "
      >
        <h3
          className="
          text-lg
          font-semibold
          "
        >
          Top Risk Services
        </h3>
      </div>

      <div
        className="
        space-y-4
        "
      >
        {risks
          .slice(0, 5)
          .map(
            (
              risk
            ) => (
              <div
                key={
                  risk.id
                }
                className="
                flex
                items-center
                justify-between
                border-b
                pb-3
                "
              >
                <div>
                  <div
                    className="
                    font-medium
                    "
                  >
                    {
                      risk.service
                    }
                  </div>

                  <div
                    className="
                    text-sm
                    text-muted-foreground
                    "
                  >
                    Customer Impact:
                    {" "}
                    {
                      risk
                        .impact_assessment
                        ?.customer_impact
                    }
                  </div>
                </div>

                <Badge>
                  {
                    risk
                      .risk_summary
                      ?.risk_level
                  }
                </Badge>
              </div>
            )
          )}
      </div>
    </Card>
  );
}