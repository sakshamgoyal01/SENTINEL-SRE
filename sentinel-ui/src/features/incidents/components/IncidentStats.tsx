import { Card } from "@/components/ui/card";

interface Props {
  incidents: any[];
}

export function IncidentStats({
  incidents,
}: Props) {

  const critical =
    incidents.filter(
      (i) =>
        i.aggregated_event
          ?.severity ===
        "CRITICAL"
    ).length;

  const avgRisk =
  incidents.length > 0
    ? (
        incidents.reduce(
          (sum, i) =>
            sum +
            i.final_risk_score,
          0
        ) /
        incidents.length
      ).toFixed(1)
    : 0;



  const escalated =
    incidents.filter(
      (i) =>
        i.escalation_required
    ).length;

  const reviews =
    incidents.filter(
      (i) =>
        i.requires_human_review
    ).length;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-5
      "
    >
      <Card className="p-4">
        Open Incidents

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {incidents.length}
        </div>
      </Card>
      <Card className="p-4">
  Avg Risk

  <div
    className="
    text-3xl
    font-bold
    "
  >
    {avgRisk}
  </div>
</Card>

      <Card className="p-4">
        Critical

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {critical}
        </div>
      </Card>

      <Card className="p-4">
        Escalated

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {escalated}
        </div>
      </Card>

      <Card className="p-4">
        Human Review

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {reviews}
        </div>
      </Card>
    </div>
  );
}