from ai.models.remediation_outcome import (
    RemediationOutcome
)


class RemediationTracker:

    def extract(
        self,
        remediation_result
    ) -> RemediationOutcome:

        actions = [

            action.action_type

            for action in
            remediation_result
            .plan
            .actions
        ]

        automated = any(

            action.automated

            for action in
            remediation_result
            .plan
            .actions
        )

        return RemediationOutcome(

            runbook=(

                remediation_result
                .plan
                .runbook
            ),

            actions=actions,

            successful=True,

            automation_used=(
                automated
            )
        )