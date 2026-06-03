import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function KnowledgeDrawer({
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
            Knowledge Entry
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
            {entry.service}
          </div>

          <div>
            <strong>
              Incident Type:
            </strong>
            {" "}
            {
              entry.pattern
                ?.incident_type
            }
          </div>

          <div>
            <strong>
              Successful:
            </strong>
            {" "}
            {entry.remediation
              ?.successful
              ? "Yes"
              : "No"}
          </div>

          <div>
            <strong>
              Knowledge ID:
            </strong>
            {" "}
            {
              entry.knowledge_id
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
