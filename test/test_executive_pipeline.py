from datetime import datetime

from ai.models.incident_pattern import (
    IncidentPattern
)

from ai.models.remediation_outcome import (
    RemediationOutcome
)

from ai.models.knowledge_record import (
    KnowledgeRecord
)

from ai.executive.executive_summary_engine import (
    ExecutiveSummaryEngine
)


def test_executive_pipeline():

    knowledge = KnowledgeRecord(

        knowledge_id="k1",

        service="payment-service",

        pattern=IncidentPattern(

            incident_type=(
                "SERVICE_DEPENDENCY"
            ),

            service=(
                "payment-service"
            ),

            severity="P1",

            root_cause=(
                "DEPENDENCY_FAILURE"
            )
        ),

        remediation=RemediationOutcome(

            runbook=(
                "RUNBOOK_DEPENDENCY_FAILURE"
            ),

            actions=[
                "VERIFY_DEPENDENCY"
            ],

            successful=True,

            automation_used=True
        ),

        created_at=(
            datetime.utcnow()
        )
    )

    engine = (
        ExecutiveSummaryEngine()
    )

    report = (
        engine.process(
            knowledge
        )
    )

    assert (
        report.service
        == "payment-service"
    )

    assert (
        report.summary
        .incident_summary
        is not None
    )

    assert (
        report.summary
        .impact_summary
        is not None
    )