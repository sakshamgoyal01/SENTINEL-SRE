import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function AuditDrawer({
  audit,
  open,
  onOpenChange,
}: {
  audit: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!audit) {
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
            Audit Details
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
            {audit.service}
          </div>

          <div>
            <strong>
              Status:
            </strong>
            {" "}
            {audit.status}
          </div>

          <div>
            <strong>
              Details:
            </strong>
            {" "}
            {audit.details}
          </div>

          <div>
            <strong>
              Audit ID:
            </strong>
            {" "}
            {audit.audit_id}
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}