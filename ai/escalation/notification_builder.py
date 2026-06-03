from ai.models.escalation_target import (
    EscalationTarget
)


class NotificationBuilder:

    def build_target(
        self,
        team: str
    ):

        return EscalationTarget(

            team=team,

            severity="HIGH",

            contact_channel=
            "SLACK"
        )