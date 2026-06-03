class BusinessImpactEstimator:

    def estimate(
        self,
        rootcause_result
    ) -> str:

        category = (

            rootcause_result
            .root_cause
            .category
        )

        mapping = {

            "Dependency Failure":
                "Revenue Impact",

            "Deployment Failure":
                "Operational Impact",

            "Network Failure":
                "Service Availability Impact",

            "Resource Exhaustion":
                "Performance Impact",

            "Configuration Drift":
                "Operational Impact"
        }

        return mapping.get(

            category,

            "Unknown Impact"
        )