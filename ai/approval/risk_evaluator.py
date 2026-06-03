class RiskEvaluator:

    def requires_human_approval(
        self,
        priority: str
    ) -> bool:

        return priority in {

            "P1",

            "P2"
        }