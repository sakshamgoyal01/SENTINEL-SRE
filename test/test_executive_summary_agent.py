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


def test_executive_summary_agent():

    knowledge_record = KnowledgeRecord(

        knowledge_id="knowledge-1",

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

                "VERIFY_DEPENDENCY",

                "ENABLE_CIRCUIT_BREAKER",

                "ESCALATE_TEAM"
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
            knowledge_record
        )
    )

    assert (
        report.service
        == "payment-service"
    )

    assert (
        "dependency-related"
        in
        report.summary
        .incident_summary
        .lower()
    )

    assert (
        "root cause identified"
        in
        report.summary
        .root_cause_summary
        .lower()
    )

    assert (
        "customer impact"
        in
        report.summary
        .impact_summary
        .lower()
    )

    assert (
        "remediation"
        in
        report.summary
        .remediation_summary
        .lower()
    )

    assert (
        report.report_id
        is not None
    )