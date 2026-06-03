class SloRiskCalculator:

    def calculate(
        self,
        rootcause_result
    ) -> float:

        severity = (
            rootcause_result
            .severity
        )

        if severity == "CRITICAL":

            return 95.0

        if severity == "HIGH":

            return 80.0

        if severity == "MEDIUM":

            return 50.0

        return 20.0