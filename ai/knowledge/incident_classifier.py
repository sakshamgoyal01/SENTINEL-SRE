class IncidentClassifier:

    def classify(
        self,
        normalized_type: str
    ) -> str:

        mapping = {

            "DEPENDENCY_FAILURE":
                "SERVICE_DEPENDENCY",

            "DEPLOYMENT_FAILURE":
                "RELEASE_FAILURE",

            "NETWORK_FAILURE":
                "NETWORK_OUTAGE",

            "RESOURCE_EXHAUSTION":
                "RESOURCE_CAPACITY"
        }

        return mapping.get(

            normalized_type,

            "UNKNOWN"
        )