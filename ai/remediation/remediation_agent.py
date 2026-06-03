import uuid

from datetime import datetime

from ai.models.remediation_result import (
    RemediationResult
)

from ai.remediation.runbook_selector import (
    RunbookSelector
)

from ai.remediation.rollback_advisor import (
    RollbackAdvisor
)

from ai.remediation.scaling_advisor import (
    ScalingAdvisor
)

from ai.remediation.action_recommender import (
    ActionRecommender
)

from ai.remediation.remediation_planner import (
    RemediationPlanner
)


class RemediationAgent:

    def __init__(self):

        self.runbook_selector = (
            RunbookSelector()
        )

        self.rollback_advisor = (
            RollbackAdvisor()
        )

        self.scaling_advisor = (
            ScalingAdvisor()
        )

        self.action_recommender = (
            ActionRecommender()
        )

        self.planner = (
            RemediationPlanner()
        )

    def analyze(
        self,
        risk_result
    ) -> RemediationResult:

        runbook = (

            self.runbook_selector
            .select(
                risk_result
            )
        )

        actions = (

            self.action_recommender
            .recommend(
                risk_result
            )
        )

        actions.extend(

            self.rollback_advisor
            .recommend(
                risk_result
            )
        )

        actions.extend(

            self.scaling_advisor
            .recommend(
                risk_result
            )
        )

        plan = (

            self.planner
            .build(

                runbook,

                actions
            )
        )

        return RemediationResult(

            remediation_id=str(
                uuid.uuid4()
            ),

            risk_id=(

                risk_result
                .risk_id
            ),

            service=(

                risk_result
                .service
            ),

            priority=(

                risk_result
                .priority
            ),

            plan=plan,

            generated_at=(
                datetime.utcnow()
            )
        )