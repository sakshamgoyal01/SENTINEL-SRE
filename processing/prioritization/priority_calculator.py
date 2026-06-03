class PriorityCalculator:

    def calculate(
        self,
        risk_score: float
    ) -> str:

        if risk_score >= 90:
            return "P1"

        if risk_score >= 75:
            return "P2"

        if risk_score >= 50:
            return "P3"

        return "P4"