from ai.models.evidence import (
    Evidence
)


class EvidenceExtractor:

    def extract(
        self,
        prioritized_event
    ) -> list[Evidence]:

        event = (
            prioritized_event
            .aggregated_event
        )

        evidence = [

            Evidence(
                evidence_type="severity",
                source="aggregation",
                description=(
                    f"Severity={event.severity}"
                )
            ),

            Evidence(
                evidence_type="risk",
                source="prioritization",
                description=(
                    f"Risk Score="
                    f"{prioritized_event.final_risk_score}"
                )
            ),

            Evidence(
                evidence_type="summary",
                source="aggregation",
                description=event.summary
            )
        ]

        if (
            prioritized_event
            .escalation_required
        ):

            evidence.append(

                Evidence(
                    evidence_type="escalation",
                    source="prioritization",
                    description=(
                        "Escalation required"
                    )
                )
            )

        if (
            prioritized_event
            .requires_human_review
        ):

            evidence.append(

                Evidence(
                    evidence_type="review",
                    source="prioritization",
                    description=(
                        "Human review required"
                    )
                )
            )

        return evidence