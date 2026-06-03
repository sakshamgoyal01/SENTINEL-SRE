import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
}
from "@/components/ui/sheet";

export function InvestigationDrawer({
  investigation,
  open,
  onOpenChange,
}: {
  investigation: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!investigation)
    return null;

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
            Investigation Details
          </SheetTitle>
        </SheetHeader>

        <div
          className="
          mt-6
          space-y-4
          "
        >
          <div>
            Service:
            {" "}
            {
              investigation.service
            }
          </div>

          <div>
            Severity:
            {" "}
            {
              investigation.severity
            }
          </div>

          <div>
            Priority:
            {" "}
            {
              investigation.priority
            }
          </div>

          <div>
            Summary:
            {" "}
            {
              investigation
                .findings
                ?.summary
            }
          </div>

          <div>
            Evidence:
            <ul
              className="
              list-disc
              ml-5
              "
            >
              {
                investigation.evidence
                  ?.map(
                    (
                      item:
                        string
                    ) => (
                      <li
                        key={
                          item
                        }
                      >
                        {item}
                      </li>
                    )
                  )
              }
            </ul>
          </div>

          <div>
            Confidence:
            {" "}
            {Math.round(
              investigation.confidence *
              100
            )}
            %
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}