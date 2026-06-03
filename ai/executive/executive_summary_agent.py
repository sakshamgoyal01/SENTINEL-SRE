import uuid

from datetime import datetime

from ai.models.executive_report import (
    ExecutiveReport
)

from ai.executive.incident_summarizer import (
    IncidentSummarizer
)

from ai.executive.impact_summarizer import (
    ImpactSummarizer
)

from ai.executive.remediation_summarizer import (
    RemediationSummarizer
)

from ai.executive.executive_summary_builder import (
    ExecutiveSummaryBuilder
)


class ExecutiveSummaryAgent:

    def __init__(self):

        self.incident = (
            IncidentSummarizer()
        )

        self.impact = (
            ImpactSummarizer()
        )

        self.remediation = (
            RemediationSummarizer()
        )

        self.builder = (
            ExecutiveSummaryBuilder()
        )

    def analyze(
        self,
        knowledge_record
    ):

        incident_summary = (

            self.incident
            .summarize(
                knowledge_record
            )
        )

        impact_summary = (

            self.impact
            .summarize(
                knowledge_record
            )
        )

        remediation_summary = (

            self.remediation
            .summarize(
                knowledge_record
            )
        )

        root_cause_summary = (

            "Root cause identified as "
            f"{knowledge_record.pattern.root_cause}."
        )

        summary = (

            self.builder.build(

                incident_summary,

                root_cause_summary,

                impact_summary,

                remediation_summary
            )
        )

        return ExecutiveReport(

            report_id=str(
                uuid.uuid4()
            ),

            service=(
                knowledge_record
                .service
            ),

            summary=summary,

            generated_at=(
                datetime.utcnow()
            )
        )