class HypothesisGenerator:

    def generate(
        self,
        indicators: list[str]
    ) -> list[str]:

        hypotheses = []

        if (
            "TIMEOUT"
            in indicators
        ):

            hypotheses.extend(

                [
                    "Dependency Failure",
                    "Network Failure"
                ]
            )

        if (
            "OOM"
            in indicators
        ):

            hypotheses.append(
                "Resource Exhaustion"
            )

        if (
            "DEPLOYMENT"
            in indicators
        ):

            hypotheses.append(
                "Deployment Failure"
            )

        if (
            "CONFIG"
            in indicators
        ):

            hypotheses.append(
                "Configuration Drift"
            )

        if (
            "DNS"
            in indicators
        ):

            hypotheses.append(
                "Network Failure"
            )

        if (
            "APPLICATION"
            in indicators
        ):

            hypotheses.append(
                "Application Regression"
            )

        return list(
            set(hypotheses)
        )