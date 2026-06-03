from ai.models.remediation_action import (
    RemediationAction
)


class ActionRecommender:

    def recommend(
        self,
        risk_result
    ) -> list[RemediationAction]:

        category = (
            risk_result
            .impact_assessment
            .operational_impact
        )

        actions = []

        if (
            category
            == "Dependency Failure"
        ):

            actions.extend([

                RemediationAction(

                    action_type=(
                        "VERIFY_DEPENDENCY"
                    ),

                    priority="IMMEDIATE",

                    description=(
                        "Verify downstream service"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "CHECK_HEALTH"
                    ),

                    priority="HIGH",

                    description=(
                        "Check dependency health"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "ENABLE_CIRCUIT_BREAKER"
                    ),

                    priority="HIGH",

                    description=(
                        "Enable circuit breaker"
                    ),

                    automated=True
                ),

                RemediationAction(

                    action_type=(
                        "ESCALATE_TEAM"
                    ),

                    priority="HIGH",

                    description=(
                        "Escalate owning team"
                    ),

                    automated=False
                )
            ])

        elif (
            category
            == "Network Failure"
        ):

            actions.extend([

                RemediationAction(

                    action_type="VERIFY_DNS",

                    priority="IMMEDIATE",

                    description=(
                        "Verify DNS resolution"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "VERIFY_SERVICE_MESH"
                    ),

                    priority="HIGH",

                    description=(
                        "Verify service mesh"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "VERIFY_INGRESS"
                    ),

                    priority="HIGH",

                    description=(
                        "Verify ingress"
                    ),

                    automated=False
                )
            ])

        elif (
            category
            == "Deployment Failure"
        ):

            actions.extend([

                RemediationAction(

                    action_type=(
                        "VERIFY_DEPLOYMENT"
                    ),

                    priority="IMMEDIATE",

                    description=(
                        "Verify deployment health"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "VALIDATE_RELEASE"
                    ),

                    priority="HIGH",

                    description=(
                        "Validate release notes"
                    ),

                    automated=False
                )
            ])

        return actions