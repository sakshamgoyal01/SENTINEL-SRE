import { Card } from "@/components/ui/card";

export function ApprovalCards({
  approvals,
  onSelect,
}: {
  approvals: any[];

  onSelect: (
    approval: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      xl:grid-cols-3
      "
    >
      {approvals.map(
        (approval) => (
          <Card
            key={approval.id}
            onClick={() =>
              onSelect(
                approval
              )
            }
            className="
            p-4
            cursor-pointer
            "
          >
            <h3
              className="
              font-bold
              "
            >
              {
                approval.service
              }
            </h3>

            <div className="mt-2">
              Approved:
              {" "}
              {
                approval.approved
                  ? "✅"
                  : "❌"
              }
            </div>

            <div className="mt-2">
              Human Review:
              {" "}
              {
                approval.requires_human_approval
                  ? "YES"
                  : "NO"
              }
            </div>

            <div className="mt-2">
              Actions:
              {" "}
              {
                approval.actions
                  ?.length
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}