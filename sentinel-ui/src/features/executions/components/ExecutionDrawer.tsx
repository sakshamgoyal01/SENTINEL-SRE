import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function ExecutionDrawer({
  execution,
  open,
  onOpenChange,
}: {
  execution: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!execution) {
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
            Execution Details
          </SheetTitle>
        </SheetHeader>

        <div
          className="
          mt-6
          space-y-4
          "
        >
          <div>
            <strong>Service:</strong>
            {" "}
            {execution.service}
          </div>

          <div>
            <strong>Status:</strong>
            {" "}
            {execution.status}
          </div>

          <div>
            <strong>Mode:</strong>
            {" "}
            {execution.mode}
          </div>

          <div>
            <strong>Executed:</strong>
            {" "}
            {execution.executed
              ? "YES"
              : "NO"}
          </div>

          <div>
            <strong>Execution ID:</strong>
            {" "}
            {
              execution.execution_id
            }
          </div>

          <div>
            <strong>Approval ID:</strong>
            {" "}
            {
              execution.approval_id
            }
          </div>

          <div>
            <strong>Actions:</strong>

            <ul
              className="
              mt-2
              list-disc
              pl-5
              "
            >
              {execution.actions?.map(
                (
                  action: any,
                  index: number
                ) => (
                  <li key={index}>
                    {
                      action.action_type
                    }
                  </li>
                )
              )}
            </ul>
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}