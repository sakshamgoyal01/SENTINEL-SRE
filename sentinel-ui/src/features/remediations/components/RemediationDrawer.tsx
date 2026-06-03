import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function RemediationDrawer({
  remediation,
  open,
  onOpenChange,
}: {
  remediation: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!remediation) {
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
            Remediation Details
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
              remediation
                .service
            }
          </div>

          <div>
            <strong>
              Priority:
            </strong>
            {" "}
            {
              remediation
                .priority
            }
          </div>

          <div>
            <strong>
              Risk ID:
            </strong>
            {" "}
            {
              remediation
                .risk_id
            }
          </div>

          <div>
            <strong>
              Remediation ID:
            </strong>
            {" "}
            {
              remediation
                .remediation_id
            }
          </div>

          <div>
            <strong>
              Runbook:
            </strong>
            {" "}
            {
              remediation
                .plan
                ?.runbook
            }
          </div>

          <div>
            <strong>
              Created:
            </strong>
            {" "}
            {new Date(
              remediation.created_at
            ).toLocaleString()}
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}