from ai.models.remediation_action import (
    RemediationAction
)


class ScalingAdvisor:

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
            != "Resource Exhaustion"
        ):

            return []

        return [

            RemediationAction(

                action_type=(
                    "SCALE_DEPLOYMENT"
                ),

                priority="HIGH",

                description=(
                    "Increase deployment replicas"
                ),

                automated=True
            )
        ]