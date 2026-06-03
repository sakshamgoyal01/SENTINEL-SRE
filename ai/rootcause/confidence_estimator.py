class ConfidenceEstimator:

    def estimate(
        self,
        investigation_result,
        indicators: list[str]
    ) -> float:

        confidence = 50.0

        if (
            "TIMEOUT"
            in indicators
        ):

            confidence += 15

        if (
            investigation_result.severity
            == "CRITICAL"
        ):

            confidence += 15

        if any(

            "Escalation"
            in finding

            for finding in
            investigation_result.findings
        ):

            confidence += 10

        if (
            investigation_result
            .confidence
            >= 90
        ):

            confidence += 10

        return min(
            confidence,
            100.0
        )