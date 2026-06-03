class CustomerImpactEstimator:

    def estimate(
        self,
        rootcause_result
    ) -> str:

        priority = (
            rootcause_result
            .priority
        )

        if priority == "P1":

            return "HIGH"

        if priority == "P2":

            return "MEDIUM"

        return "LOW"