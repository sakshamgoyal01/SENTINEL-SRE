import { Card }
from "@/components/ui/card";

export function InvestigationStats({
  investigations,
}: {
  investigations: any[];
}) {

  const critical =
    investigations.filter(
      (i) =>
        i.severity ===
        "CRITICAL"
    ).length;

  const avgConfidence =
    investigations.length > 0
      ? (
          investigations.reduce(
            (
              sum,
              item
            ) =>
              sum +
              item.confidence,
            0
          ) /
          investigations.length
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
        Open Investigations

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {
            investigations.length
          }
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
        Avg Confidence

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {avgConfidence}
        </div>
      </Card>

      <Card className="p-4">
        Services Impacted

        <div
          className="
          text-3xl
          font-bold
          "
        >
          {
            new Set(
              investigations.map(
                (i) =>
                  i.service
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}