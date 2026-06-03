import { Card } from "@/components/ui/card";

export function EscalationCards({
  escalations,
  onSelect,
}: {
  escalations: any[];

  onSelect: (
    escalation: any
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
      {escalations.map(
        (escalation) => (
          <Card
            key={
              escalation.id
            }
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                escalation
              )
            }
          >
            <h3
              className="
              font-semibold
              "
            >
              {
                escalation.service
              }
            </h3>

            <div className="mt-2">
              {
                escalation
                  .escalation_reason
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              text-muted-foreground
              "
            >
              Team:
              {" "}
              {
                escalation
                  .target?.team
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}