class FailureAnalyzer:

    def analyze(
        self,
        verification_result
    ) -> str:

        if (
            verification_result
            .verified
        ):

            return "HEALTHY"

        return (
            verification_result
            .health_status
        )