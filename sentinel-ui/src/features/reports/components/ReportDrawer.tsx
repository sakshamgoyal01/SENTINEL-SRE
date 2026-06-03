import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function ReportDrawer({
  report,
  open,
  onOpenChange,
}: {
  report: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!report) {
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
            Report Details
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
            {report.service}
          </div>

          <div>
            <strong>
              Report ID:
            </strong>
            {" "}
            {
              report.report_id
            }
          </div>

          <div>
            <strong>
              Summary:
            </strong>
            {" "}
            {
              report.summary
                ?.incident_summary
            }
          </div>

          <div>
            <strong>
              Generated:
            </strong>
            {" "}
            {
              report.generated_at
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
