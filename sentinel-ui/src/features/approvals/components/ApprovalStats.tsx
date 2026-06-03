import { Card } from "@/components/ui/card";

export function ApprovalStats({
  approvals,
}: {
  approvals: any[];
}) {
  const approved =
    approvals.filter(
      (a) => a.approved
    ).length;

  const humanReview =
    approvals.filter(
      (a) =>
        a.requires_human_approval
    ).length;

  const actions =
    approvals.reduce(
      (
        total,
        approval
      ) =>
        total +
        (
          approval.actions
            ?.length ?? 0
        ),
      0
    );

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Total

        <div className="text-3xl font-bold">
          {approvals.length}
        </div>
      </Card>

      <Card className="p-4">
        Approved

        <div className="text-3xl font-bold">
          {approved}
        </div>
      </Card>

      <Card className="p-4">
        Human Review

        <div className="text-3xl font-bold">
          {humanReview}
        </div>
      </Card>

      <Card className="p-4">
        Actions

        <div className="text-3xl font-bold">
          {actions}
        </div>
      </Card>
    </div>
  );
}