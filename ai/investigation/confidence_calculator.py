class ConfidenceCalculator:

    def calculate(
        self,
        prioritized_event
    ) -> float:

        confidence = 50.0

        event = (
            prioritized_event
            .aggregated_event
        )

        if event.severity == "CRITICAL":

            confidence += 20

        if (
            prioritized_event
            .final_risk_score >= 90
        ):

            confidence += 10

        if (
            prioritized_event
            .escalation_required
        ):

            confidence += 10

        if (
            prioritized_event
            .requires_human_review
        ):

            confidence += 10

        return min(
            confidence,
            100
        )