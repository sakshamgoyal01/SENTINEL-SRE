import { Card } from "@/components/ui/card";

export function RemediationCards({
  remediations,
  onSelect,
}: {
  remediations: any[];
  onSelect: (
    remediation: any
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
      {remediations.map(
        (remediation) => (
          <Card
            key={
              remediation.id
            }
            onClick={() =>
              onSelect(
                remediation
              )
            }
            className="
            p-4
            cursor-pointer
            "
          >
            <h3
              className="
              font-bold
              "
            >
              {
                remediation.service
              }
            </h3>

            <div
              className="
              mt-3
              text-sm
              "
            >
              Priority:
              {" "}
              {
                remediation.priority
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              "
            >
              Runbook:
              {" "}
              {
                remediation
                  .plan
                  ?.runbook
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}