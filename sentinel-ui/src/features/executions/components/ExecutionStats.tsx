import { Card } from "@/components/ui/card";

export function ExecutionStats({
  executions,
}: {
  executions: any[];
}) {

  const success =
    executions.filter(
      (e) =>
        e.status ===
        "SUCCESS"
    ).length;

  const executed =
    executions.filter(
      (e) =>
        e.executed
    ).length;

  const dryRun =
    executions.filter(
      (e) =>
        e.mode ===
        "DRY_RUN"
    ).length;

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
          {executions.length}
        </div>
      </Card>

      <Card className="p-4">
        Executed

        <div className="text-3xl font-bold">
          {executed}
        </div>
      </Card>

      <Card className="p-4">
        Success

        <div className="text-3xl font-bold">
          {success}
        </div>
      </Card>

      <Card className="p-4">
        Dry Runs

        <div className="text-3xl font-bold">
          {dryRun}
        </div>
      </Card>
    </div>
  );
}