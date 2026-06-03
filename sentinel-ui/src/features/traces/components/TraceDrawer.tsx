import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function TraceDrawer({
  trace,
  open,
  onOpenChange,
}: {
  trace: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!trace) {
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
            Trace Details
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
              Operation:
            </strong>
            {" "}
            {
              trace.operation
            }
          </div>

          <div>
            <strong>
              Service:
            </strong>
            {" "}
            {
              trace.service
            }
          </div>

          <div>
            <strong>
              Duration:
            </strong>
            {" "}
            {
              trace.duration_ms
            }
            ms
          </div>

          <div>
            <strong>
              Status:
            </strong>
            {" "}
            {
              trace.status_code
            }
          </div>

          <div>
            <strong>
              Trace ID:
            </strong>
            {" "}
            {
              trace.trace_id
            }
          </div>

          <div>
            <strong>
              Span ID:
            </strong>
            {" "}
            {
              trace.span_id
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}