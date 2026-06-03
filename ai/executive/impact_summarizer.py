class ImpactSummarizer:

    def summarize(
        self,
        knowledge_record
    ) -> str:

        severity = (
            knowledge_record
            .pattern
            .severity
        )

        if severity == "P1":

            return (

                "Customer impact is high "
                "with elevated SLO "
                "violation risk."
            )

        if severity == "P2":

            return (

                "Customer impact is "
                "moderate with potential "
                "service degradation."
            )

        return (

            "Customer impact is low "
            "with limited service "
            "degradation."
        )