import {
  Card,
} from "@/components/ui/card";

export function SystemHealth({
  alerts,
  incidents,
  risks,
}: {
  alerts: any[];
  incidents: any[];
  risks: any[];
}) {

  const criticalAlerts =
    alerts.filter(
      (
        alert
      ) =>
        alert.severity ===
        "CRITICAL"
    ).length;

  const criticalRisks =
    risks.filter(
      (
        risk
      ) =>
        risk
          .risk_summary
          ?.risk_level ===
        "CRITICAL"
    ).length;

  const activeIncidents =
    incidents.length;

  const score =
    Math.max(
      0,
      100 -
        (
          criticalAlerts *
            5 +
          criticalRisks *
            5 +
          activeIncidents *
            3
        )
    );

  const status =
    score > 80
      ? "Healthy"
      : score > 50
      ? "Warning"
      : "Critical";

  return (
    <Card
      className="
      p-6
      "
    >
      <div
        className="
        flex
        items-center
        justify-between
        "
      >
        <div>
          <h3
            className="
            text-lg
            font-semibold
            "
          >
            System Health
          </h3>

          <p
            className="
            text-sm
            text-muted-foreground
            "
          >
            Overall platform
            status
          </p>
        </div>

        <div
          className="
          text-right
          "
        >
          <div
            className="
            text-4xl
            font-bold
            "
          >
            {score}
          </div>

          <div
            className="
            text-sm
            text-muted-foreground
            "
          >
            Score
          </div>
        </div>
      </div>

      <div
        className="
        mt-6
        "
      >
        <div
          className="
          text-xl
          font-semibold
          "
        >
          {status}
        </div>
      </div>

      <div
        className="
        mt-6
        grid
        grid-cols-3
        gap-4
        "
      >
        <div>
          <p
            className="
            text-sm
            text-muted-foreground
            "
          >
            Alerts
          </p>

          <h2
            className="
            text-xl
            font-bold
            "
          >
            {
              criticalAlerts
            }
          </h2>
        </div>

        <div>
          <p
            className="
            text-sm
            text-muted-foreground
            "
          >
            Risks
          </p>

          <h2
            className="
            text-xl
            font-bold
            "
          >
            {
              criticalRisks
            }
          </h2>
        </div>

        <div>
          <p
            className="
            text-sm
            text-muted-foreground
            "
          >
            Incidents
          </p>

          <h2
            className="
            text-xl
            font-bold
            "
          >
            {
              activeIncidents
            }
          </h2>
        </div>
      </div>
    </Card>
  );
}