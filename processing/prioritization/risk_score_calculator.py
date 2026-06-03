class RiskScoreCalculator:

    def calculate(
        self,
        aggregated_event,
        impact_score: float
    ) -> float:

        return round(

            (
                aggregated_event.risk_score
                * 0.6
            )

            +

            (
                impact_score
                * 0.4
            ),

            2
        )