import { Card } from "@/components/ui/card";

export function RootCauseCards({
  rootCauses,
  onSelect,
}: {
  rootCauses: any[];

  onSelect: (
    rootCause: any
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
      {rootCauses.map(
        (rootCause) => (
          <Card
            key={rootCause.id}
            onClick={() =>
              onSelect(
                rootCause
              )
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
              {
                rootCause
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
                rootCause
                  .root_cause
                  ?.cause_type
              }
            </h3>

            <p
              className="
              mt-2
              text-sm
              text-muted-foreground
              "
            >
              {
                rootCause
                  .service
              }
            </p>

            <div
              className="
              mt-4
              space-y-2
              text-sm
              "
            >
              <div>
                Confidence:
                {" "}
                {Math.round(
                  rootCause.confidence *
                  100
                )}
                %
              </div>

              <div>
                Trigger:
                {" "}
                {
                  rootCause
                    .causal_chain
                    ?.trigger
                }
              </div>

              <div>
                Severity:
                {" "}
                {
                  rootCause
                    .severity
                }
              </div>
            </div>
          </Card>
        )
      )}
    </div>
  );
}