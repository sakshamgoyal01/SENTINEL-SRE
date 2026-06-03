class RootCauseClassifier:

    def classify(
        self,
        indicators: list[str]
    ):

        if (
            "TIMEOUT"
            in indicators
        ):

            return (

                "Dependency Failure",

                "Downstream dependency timeout"
            )

        if (
            "OOM"
            in indicators
        ):

            return (

                "Resource Exhaustion",

                "Memory pressure detected"
            )

        if (
            "DEPLOYMENT"
            in indicators
        ):

            return (

                "Deployment Failure",

                "Recent deployment introduced instability"
            )

        if (
            "CONFIG"
            in indicators
        ):

            return (

                "Configuration Drift",

                "Configuration inconsistency detected"
            )

        if (
            "DNS"
            in indicators
        ):

            return (

                "Network Failure",

                "DNS resolution issue detected"
            )

        return (

            "Unknown",

            "Unable to determine root cause"
        )