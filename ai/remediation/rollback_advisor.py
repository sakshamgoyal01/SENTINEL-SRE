from ai.models.remediation_action import (
    RemediationAction
)


class RollbackAdvisor:

    def recommend(
        self,
        risk_result
    ) -> list[RemediationAction]:

        category = (
            risk_result
            .impact_assessment
            .operational_impact
        )

        if (
            category
            != "Deployment Failure"
        ):

            return []

        return [

            RemediationAction(

                action_type=(
                    "ROLLBACK_DEPLOYMENT"
                ),

                priority="IMMEDIATE",

                description=(
                    "Rollback latest deployment"
                ),

                automated=False
            )
        ]