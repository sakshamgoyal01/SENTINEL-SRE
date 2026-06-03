import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function RecoveryDrawer({
  recovery,
  open,
  onOpenChange,
}: {
  recovery: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!recovery) {
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
            Recovery Details
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
              recovery.service
            }
          </div>

          <div>
            <strong>
              Recovery Status:
            </strong>
            {" "}
            {
              recovery
                .recovery_status
            }
          </div>

          <div>
            <strong>
              Strategy:
            </strong>
            {" "}
            {
              recovery
                .strategy
                ?.type
            }
          </div>

          <div>
            <strong>
              Recovery ID:
            </strong>
            {" "}
            {
              recovery
                .recovery_id
            }
          </div>

          <div>
            <strong>
              Verification ID:
            </strong>
            {" "}
            {
              recovery
                .verification_id
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}