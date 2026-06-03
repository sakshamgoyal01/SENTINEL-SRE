from ai.models.causal_chain import (
    CausalChain
)


class CausalChainBuilder:

    def build(
        self,
        category: str
    ) -> CausalChain:

        if (
            category
            == "Dependency Failure"
        ):

            return CausalChain(

                chain=[

                    "Dependency latency increased",

                    "Application requests timed out",

                    "Error volume increased",

                    "Critical incident triggered"
                ]
            )

        if (
            category
            == "Resource Exhaustion"
        ):

            return CausalChain(

                chain=[

                    "Memory utilization increased",

                    "Container became unstable",

                    "Service availability degraded",

                    "Critical incident triggered"
                ]
            )

        if (
            category
            == "Deployment Failure"
        ):

            return CausalChain(

                chain=[

                    "Deployment introduced change",

                    "Application behavior regressed",

                    "Error rate increased",

                    "Critical incident triggered"
                ]
            )

        return CausalChain(

            chain=[

                "Unknown trigger observed",

                "Incident generated"
            ]
        )