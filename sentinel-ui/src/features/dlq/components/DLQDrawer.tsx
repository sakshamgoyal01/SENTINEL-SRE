import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function DLQDrawer({
  entry,
  open,
  onOpenChange,
}: {
  entry: any;
  open: boolean;
  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!entry) {
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
            DLQ Event
          </SheetTitle>
        </SheetHeader>

        <div
          className="
          mt-6
          space-y-3
          "
        >
          <div>
            Service:
            {" "}
            {
              entry.payload
                ?.service
            }
          </div>

          <div>
            Topic:
            {" "}
            {
              entry.source_topic
            }
          </div>

          <div>
            Error:
            {" "}
            {
              entry.error_message
            }
          </div>

          <div>
            DLQ ID:
            {" "}
            {
              entry.dlq_id
            }
          </div>

          <div>
            Created:
            {" "}
            {
              entry.created_at
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
