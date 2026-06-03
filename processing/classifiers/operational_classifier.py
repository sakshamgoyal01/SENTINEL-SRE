class OperationalClassifier:

    def classify(
        self,
        event
    ) -> str:

        category = (
            event.category.lower()
        )

        if category == "performance":

            return "latency_issue"

        if category == "availability":

            return "dependency_failure"

        if category == "deployment":

            return "deployment_risk"

        if category == "infrastructure":

            return "resource_pressure"

        if category == "security":

            return "security_incident"

        return "observability_event"