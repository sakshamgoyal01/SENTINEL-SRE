from ai.models.executive_summary import (
    ExecutiveSummary
)


class ExecutiveSummaryBuilder:

    def build(

        self,

        incident_summary: str,

        root_cause_summary: str,

        impact_summary: str,

        remediation_summary: str
    ) -> ExecutiveSummary:

        return ExecutiveSummary(

            incident_summary=(
                incident_summary
            ),

            root_cause_summary=(
                root_cause_summary
            ),

            impact_summary=(
                impact_summary
            ),

            remediation_summary=(
                remediation_summary
            )
        )