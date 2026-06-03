class MttrPredictor:

    def predict(
        self,
        rootcause_result
    ) -> int:

        category = (

            rootcause_result
            .root_cause
            .category
        )

        mapping = {

            "Dependency Failure": 45,

            "Network Failure": 60,

            "Deployment Failure": 30,

            "Resource Exhaustion": 20,

            "Configuration Drift": 25,

            "Unknown": 90
        }

        return mapping.get(
            category,
            90
        )