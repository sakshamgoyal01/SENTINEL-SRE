import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function ApprovalDrawer({
  approval,
  open,
  onOpenChange,
}: {
  approval: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!approval) {
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
            Approval Details
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
            {
              approval.service
            }
          </div>

          <div>
            <strong>
              Approved:
            </strong>
            {" "}
            {approval.approved
              ? "YES"
              : "NO"}
          </div>

          <div>
            <strong>
              Human Approval:
            </strong>
            {" "}
            {approval.requires_human_approval
              ? "YES"
              : "NO"}
          </div>

          <div>
            <strong>
              Reason:
            </strong>
            {" "}
            {
              approval.reason
            }
          </div>

          <div>
            <strong>
              Approval ID:
            </strong>
            {" "}
            {
              approval
                .approval_id
            }
          </div>

          <div>
            <strong>
              Generated:
            </strong>
            {" "}
            {new Date(
              approval.generated_at
            ).toLocaleString()}
          </div>

          <div>
            <strong>
              Actions:
            </strong>

            <ul
              className="
              mt-2
              list-disc
              pl-5
              "
            >
              {approval.actions?.map(
                (
                  action: any,
                  index: number
                ) => (
                  <li
                    key={index}
                  >
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