import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function AlertDrawer({
  alert,
  open,
  onOpenChange,
}: {
  alert: any;
  open: boolean;
  onOpenChange: (v: boolean) => void;
}) {
  if (!alert) return null;

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
            Alert Details
          </SheetTitle>
        </SheetHeader>

        <div className="mt-6 space-y-4">
          <div>
            <strong>Title:</strong>{" "}
            {alert.title}
          </div>

          <div>
            <strong>Severity:</strong>{" "}
            {alert.severity}
          </div>

          <div>
            <strong>Status:</strong>{" "}
            {alert.status}
          </div>

          <div>
            <strong>Service:</strong>{" "}
            {alert.service}
          </div>

          <div>
            <strong>Description:</strong>{" "}
            {alert.description}
          </div>

          <div>
            <strong>Source:</strong>{" "}
            {alert.source}
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
