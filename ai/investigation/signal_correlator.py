class SignalCorrelator:

    def correlate(
        self,
        prioritized_event
    ) -> list[str]:

        findings = []

        event = (
            prioritized_event
            .aggregated_event
        )

        if event.severity == "CRITICAL":

            findings.append(
                "Critical incident detected"
            )

        if (
            prioritized_event
            .final_risk_score >= 90
        ):

            findings.append(
                "High risk score observed"
            )

        if (
            prioritized_event
            .escalation_required
        ):

            findings.append(
                "Escalation required"
            )

        if (
            prioritized_event
            .requires_human_review
        ):

            findings.append(
                "Human review required"
            )

        if event.count > 50:

            findings.append(
                "Large aggregation burst detected"
            )

        return findings