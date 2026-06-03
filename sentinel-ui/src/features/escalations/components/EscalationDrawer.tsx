import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function EscalationDrawer({
  escalation,
  open,
  onOpenChange,
}: {
  escalation: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!escalation) {
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
            Escalation Details
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
              escalation.service
            }
          </div>

          <div>
            <strong>
              Team:
            </strong>
            {" "}
            {
              escalation
                .target?.team
            }
          </div>

          <div>
            <strong>
              Reason:
            </strong>
            {" "}
            {
              escalation
                .escalation_reason
            }
          </div>

          <div>
            <strong>
              Recovery:
            </strong>
            {" "}
            {
              escalation
                .recovery_id
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}