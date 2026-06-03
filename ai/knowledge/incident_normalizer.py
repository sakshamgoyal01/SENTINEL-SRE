class IncidentNormalizer:

    def normalize(
        self,
        runbook: str
    ) -> str:

        runbook = runbook.upper()

        if (
            "DEPENDENCY"
            in runbook
        ):

            return (
                "DEPENDENCY_FAILURE"
            )

        if (
            "ROLLBACK"
            in runbook
        ):

            return (
                "DEPLOYMENT_FAILURE"
            )

        if (
            "NETWORK"
            in runbook
        ):

            return (
                "NETWORK_FAILURE"
            )

        if (
            "RESOURCE"
            in runbook
        ):

            return (
                "RESOURCE_EXHAUSTION"
            )

        return "UNKNOWN"