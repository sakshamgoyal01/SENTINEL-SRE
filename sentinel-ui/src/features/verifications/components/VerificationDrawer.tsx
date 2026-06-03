import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function VerificationDrawer({
  verification,
  open,
  onOpenChange,
}: {
  verification: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (
    !verification
  ) {
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
            Verification Details
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
              Service:
            </strong>
            {" "}
            {
              verification.service
            }
          </div>

          <div>
            <strong>
              Result:
            </strong>
            {" "}
            {
              verification
                .verification_result
            }
          </div>

          <div>
            <strong>
              Health:
            </strong>
            {" "}
            {
              verification
                .health_status
            }
          </div>

          <div>
            <strong>
              Verified:
            </strong>
            {" "}
            {
              verification.verified
                ? "Yes"
                : "No"
            }
          </div>

          <div>
            <strong>
              Execution:
            </strong>
            {" "}
            {
              verification
                .execution_id
            }
          </div>

          <div>
            <strong>
              Checks:
            </strong>
          </div>

          <ul
            className="
            list-disc
            ml-5
            "
          >
            {verification.checks?.map(
              (
                check: any,
                index: number
              ) => (
                <li
                  key={index}
                >
                  {
                    check.check
                  }
                </li>
              )
            )}
          </ul>
        </div>
      </SheetContent>
    </Sheet>
  );
}