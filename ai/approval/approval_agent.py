import uuid

from datetime import datetime

from ai.models.approval_action import (
    ApprovalAction
)

from ai.models.approval_decision import (
    ApprovalDecision
)

from ai.approval.policy_engine import (
    PolicyEngine
)

from ai.approval.risk_evaluator import (
    RiskEvaluator
)

from ai.approval.environment_evaluator import (
    EnvironmentEvaluator
)


class ApprovalAgent:

    def __init__(self):

        self.policy_engine = (
            PolicyEngine()
        )

        self.risk_evaluator = (
            RiskEvaluator()
        )

        self.environment = (
            EnvironmentEvaluator()
        )

    def analyze(
        self,
        remediation_result
    ) -> ApprovalDecision:

        actions = []

        approval_required = (

            self.risk_evaluator
            .requires_human_approval(

                remediation_result
                .priority
            )
        )

        denied = False

        reason = (
            "Automatically approved"
        )

        for action in (

            remediation_result
            .plan
            .actions
        ):

            decision = (

                self.policy_engine
                .evaluate(
                    action.action_type
                )
            )

            actions.append(

                ApprovalAction(

                    action_type=(
                        action.action_type
                    ),

                    priority=(
                        action.priority
                    ),

                    automated=(
                        action.automated
                    )
                )
            )

            if decision == "DENY":

                denied = True

                reason = (

                    f"{action.action_type} "
                    f"is prohibited"
                )

            elif decision == "HUMAN":

                approval_required = True

                reason = (

                    f"{action.action_type} "
                    f"requires human approval"
                )

        if (

            remediation_result
            .priority
            in {"P1", "P2"}
        ):

            approval_required = True

            reason = (

                f"{remediation_result.priority} "
                f"incident requires "
                f"human approval"
            )

        approved = (

            not denied
            and
            not approval_required
        )

        return ApprovalDecision(

            approval_id=str(
                uuid.uuid4()
            ),

            service=(
                remediation_result
                .service
            ),

            approved=approved,

            requires_human_approval=(
                approval_required
            ),

            reason=reason,

            actions=actions,

            generated_at=(
                datetime.utcnow()
            )
        )