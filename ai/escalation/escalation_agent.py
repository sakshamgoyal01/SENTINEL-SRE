import uuid

from datetime import datetime

from ai.models.escalation_record import (
    EscalationRecord
)

from ai.escalation.escalation_evaluator import (
    EscalationEvaluator
)

from ai.escalation.severity_analyzer import (
    SeverityAnalyzer
)

from ai.escalation.notification_builder import (
    NotificationBuilder
)


class EscalationAgent:

    def __init__(self):

        self.evaluator = (
            EscalationEvaluator()
        )

        self.analyzer = (
            SeverityAnalyzer()
        )

        self.builder = (
            NotificationBuilder()
        )

    def process(
        self,
        recovery_result
    ):

        should_escalate = (

            self.evaluator
            .should_escalate(
                recovery_result
            )
        )

        if not should_escalate:

            return None

        team = (

            self.analyzer
            .determine_team(
                recovery_result
                .service
            )
        )

        target = (

            self.builder
            .build_target(
                team
            )
        )

        return EscalationRecord(

            escalation_id=str(
                uuid.uuid4()
            ),

            service=(
                recovery_result
                .service
            ),

            recovery_id=(
                recovery_result
                .recovery_id
            ),

            escalation_reason=(
                recovery_result
                .strategy
                .reason
            ),

            target=target,

            generated_at=(
                datetime.utcnow()
            )
        )