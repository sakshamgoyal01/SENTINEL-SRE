import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function RootCauseDrawer({
  rootCause,
  open,
  onOpenChange,
}: {
  rootCause: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!rootCause) {
    return null;
  }

  return (
    <Sheet
      open={open}
      onOpenChange={
        onOpenChange
      }
    >
      <SheetContent>
        <SheetHeader>
          <SheetTitle>
            Root Cause Details
          </SheetTitle>
        </SheetHeader>

        <div
          className="
          mt-6
          space-y-4
          "
        >
          <div>
            <strong>
              Cause Type:
            </strong>
            {" "}
            {
              rootCause
                .root_cause
                ?.cause_type
            }
          </div>

          <div>
            <strong>
              Service:
            </strong>
            {" "}
            {
              rootCause
                .service
            }
          </div>

          <div>
            <strong>
              Severity:
            </strong>
            {" "}
            {
              rootCause
                .severity
            }
          </div>

          <div>
            <strong>
              Priority:
            </strong>
            {" "}
            {
              rootCause
                .priority
            }
          </div>

          <div>
            <strong>
              Confidence:
            </strong>
            {" "}
            {Math.round(
              rootCause.confidence *
              100
            )}
            %
          </div>

          <div>
            <strong>
              Trigger:
            </strong>
            {" "}
            {
              rootCause
                .causal_chain
                ?.trigger
            }
          </div>

          <div>
            <strong>
              Investigation ID:
            </strong>
            {" "}
            {
              rootCause
                .investigation_id
            }
          </div>

          <div>
            <strong>
              Evidence:
            </strong>

            <ul
              className="
              mt-2
              list-disc
              pl-5
              "
            >
              {rootCause.evidence?.map(
                (
                  item: string
                ) => (
                  <li key={item}>
                    {item}
                  </li>
                )
              )}
            </ul>
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}