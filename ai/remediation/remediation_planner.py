from ai.models.remediation_plan import (
    RemediationPlan
)


class RemediationPlanner:

    def build(

        self,

        runbook: str,

        actions
    ) -> RemediationPlan:

        return RemediationPlan(

            runbook=runbook,

            actions=actions
        )