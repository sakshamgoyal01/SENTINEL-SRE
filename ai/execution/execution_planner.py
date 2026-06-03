from ai.models.execution_action import (
    ExecutionAction
)


class ExecutionPlanner:

    def build_actions(

        self,

        approval_decision
    ):

        actions = []

        for action in (

            approval_decision
            .actions
        ):

            actions.append(

                ExecutionAction(

                    action_type=(
                        action.action_type
                    ),

                    target=(
                        approval_decision
                        .service
                    ),

                    mode="DRY_RUN"
                )
            )

        return actions