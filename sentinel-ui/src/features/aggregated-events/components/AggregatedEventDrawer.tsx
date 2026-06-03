import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function AggregatedEventDrawer({
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
            Aggregated Event
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
              Category:
            </strong>
            {" "}
            {
              event.category
            }
          </div>

          <div>
            <strong>
              Severity:
            </strong>
            {" "}
            {
              event.severity
            }
          </div>

          <div>
            <strong>
              Count:
            </strong>
            {" "}
            {
              event.count
            }
          </div>

          <div>
            <strong>
              Summary:
            </strong>
            {" "}
            {
              event.summary
            }
          </div>

          <div>
            <strong>
              Services:
            </strong>
            {" "}
            {
              event.services.join(
                ", "
              )
            }
          </div>

          <div>
            <strong>
              Aggregation Key:
            </strong>
            {" "}
            {
              event.aggregation_key
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
