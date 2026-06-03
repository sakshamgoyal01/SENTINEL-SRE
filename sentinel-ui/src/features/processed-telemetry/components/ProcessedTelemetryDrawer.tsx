import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function ProcessedTelemetryDrawer({
  telemetry,
  open,
  onOpenChange,
}: {
  telemetry: any;
  open: boolean;
  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!telemetry) {
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
            Processed Event
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
              telemetry.service
            }
          </div>

          <div>
            Type:
            {" "}
            {
              telemetry.event_type
            }
          </div>

          <div>
            Category:
            {" "}
            {
              telemetry.category
            }
          </div>

          <div>
            Severity:
            {" "}
            {
              telemetry.severity
            }
          </div>

          <div>
            Risk:
            {" "}
            {
              telemetry.risk_score
            }
          </div>

          <div>
            Summary:
            {" "}
            {
              telemetry.summary
            }
          </div>

          <div>
            Metric:
            {" "}
            {
              telemetry.raw_event
                ?.metric_name
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
