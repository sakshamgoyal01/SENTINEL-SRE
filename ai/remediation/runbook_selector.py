class RunbookSelector:

    def select(
        self,
        risk_result
    ) -> str:

        category = (
            risk_result
            .impact_assessment
            .operational_impact
        )

        mapping = {

            "Dependency Failure":
                "RUNBOOK_DEPENDENCY_FAILURE",

            "Deployment Failure":
                "RUNBOOK_ROLLBACK",

            "Network Failure":
                "RUNBOOK_NETWORK_RECOVERY",

            "Resource Exhaustion":
                "RUNBOOK_RESOURCE_SCALING",

            "Configuration Drift":
                "RUNBOOK_CONFIGURATION_RECOVERY"
        }

        return mapping.get(

            category,

            "RUNBOOK_GENERIC_INCIDENT"
        )