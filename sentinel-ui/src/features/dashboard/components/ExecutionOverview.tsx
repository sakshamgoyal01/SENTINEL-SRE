import {
  Card,
} from "@/components/ui/card";

import {
  Progress,
} from "@/components/ui/progress";

export function ExecutionOverview({
  executions,
}: {
  executions: any[];
}) {

  const total =
    executions.length;

  const successful =
    executions.filter(
      (
        execution
      ) =>
        execution.status ===
        "SUCCESS"
    ).length;

  const failed =
    executions.filter(
      (
        execution
      ) =>
        execution.status ===
        "FAILED"
    ).length;

  const successRate =
    total === 0
      ? 0
      : Math.round(
          (
            successful /
            total
          ) *
            100
        );

  return (
    <Card
      className="
      p-6
      "
    >
      <div
        className="
        mb-4
        "
      >
        <h3
          className="
          text-lg
          font-semibold
          "
        >
          Execution Overview
        </h3>

        <p
          className="
          text-sm
          text-muted-foreground
          "
        >
          Autonomous remediation
          performance
        </p>
      </div>

      <div
        className="
        space-y-5
        "
      >
        <div>
          <div
            className="
            flex
            justify-between
            mb-2
            "
          >
            <span>
              Success Rate
            </span>

            <span>
              {
                successRate
              }
              %
            </span>
          </div>

          <Progress
            value={
              successRate
            }
          />
        </div>

        <div
          className="
          grid
          grid-cols-3
          gap-4
          "
        >
          <div>
            <p
              className="
              text-sm
              text-muted-foreground
              "
            >
              Total
            </p>

            <h2
              className="
              text-2xl
              font-bold
              "
            >
              {total}
            </h2>
          </div>

          <div>
            <p
              className="
              text-sm
              text-muted-foreground
              "
            >
              Success
            </p>

            <h2
              className="
              text-2xl
              font-bold
              "
            >
              {
                successful
              }
            </h2>
          </div>

          <div>
            <p
              className="
              text-sm
              text-muted-foreground
              "
            >
              Failed
            </p>

            <h2
              className="
              text-2xl
              font-bold
              "
            >
              {failed}
            </h2>
          </div>
        </div>
      </div>
    </Card>
  );
}