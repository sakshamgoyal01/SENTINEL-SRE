class ImpactEstimator:

    def estimate(
        self,
        aggregated_event
    ) -> float:

        score = 0

        score += min(
            aggregated_event.count,
            100
        ) * 0.3

        score += (
            aggregated_event.risk_score
            * 0.5
        )

        score += (
            len(
                aggregated_event.services
            )
            * 10
        )

        return min(
            round(score, 2),
            100
        )