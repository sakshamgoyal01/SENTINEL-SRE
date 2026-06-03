import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function StateDrawer({
  state,
  open,
  onOpenChange,
}: {
  state: any;
  open: boolean;
  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!state) {
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
            Incident State
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
            {state.service}
          </div>

          <div>
            <strong>
              State:
            </strong>
            {" "}
            {
              state.current_state
            }
          </div>

          <div>
            <strong>
              Incident:
            </strong>
            {" "}
            {
              state.incident_id
            }
          </div>

          <div>
            <strong>
              Topic:
            </strong>
            {" "}
            {
              state.source_topic
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
