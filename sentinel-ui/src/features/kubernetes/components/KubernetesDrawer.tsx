import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function KubernetesDrawer({
  event,
  open,
  onOpenChange,
}: {
  event: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!event) {
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
            Kubernetes Event
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
              Type:
            </strong>
            {" "}
            {
              event.event_type
            }
          </div>

          <div>
            <strong>
              Reason:
            </strong>
            {" "}
            {
              event.reason
            }
          </div>

          <div>
            <strong>
              Object:
            </strong>
            {" "}
            {
              event
                .involved_object
                ?.kind
            }
            /
            {
              event
                .involved_object
                ?.name
            }
          </div>

          <div>
            <strong>
              Message:
            </strong>
            {" "}
            {
              event.message
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}