import { Card }
from "@/components/ui/card";

export function InvestigationCards({
  investigations,
  onSelect,
}: {
  investigations: any[];

  onSelect: (
    investigation: any
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
      {investigations.map(
        (
          investigation
        ) => (
          <Card
            key={
              investigation.id
            }
            onClick={() =>
              onSelect(
                investigation
              )
            }
            className="
            p-4
            cursor-pointer
            "
          >
            <div
              className="
              text-sm
              font-medium
              "
            >
              {
                investigation
                  .priority
              }
            </div>

            <h3
              className="
              mt-2
              font-bold
              "
            >
              {
                investigation
                  .service
              }
            </h3>

            <p
              className="
              mt-2
              text-sm
              "
            >
              {
                investigation
                  .findings
                  ?.summary
              }
            </p>

            <div
              className="
              mt-4
              text-sm
              "
            >
              Confidence:
              {" "}
              {Math.round(
                investigation.confidence *
                100
              )}
              %
            </div>
          </Card>
        )
      )}
    </div>
  );
}