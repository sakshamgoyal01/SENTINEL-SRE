import uuid

from datetime import datetime

from ai.models.execution_result import (
    ExecutionResult
)

from ai.execution.execution_planner import (
    ExecutionPlanner
)

from ai.execution.dry_run_executor import (
    DryRunExecutor
)


class ExecutionAgent:

    def __init__(self):

        self.planner = (
            ExecutionPlanner()
        )

        self.executor = (
            DryRunExecutor()
        )

    def execute(
        self,
        approval_decision
    ):

        actions = (

            self.planner
            .build_actions(
                approval_decision
            )
        )

        result = (

            self.executor
            .execute(
                actions
            )
        )

        return ExecutionResult(

            execution_id=str(
                uuid.uuid4()
            ),

            service=(
                approval_decision
                .service
            ),

            executed=(
                result["executed"]
            ),

            status=(
                result["status"]
            ),

            mode="DRY_RUN",

            actions=actions,

            generated_at=(
                datetime.utcnow()
            )
        )