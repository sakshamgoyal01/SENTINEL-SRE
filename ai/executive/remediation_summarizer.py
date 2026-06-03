class RemediationSummarizer:

    def summarize(
        self,
        knowledge_record
    ) -> str:

        runbook = (

            knowledge_record
            .remediation
            .runbook
        )

        mapping = {

            "RUNBOOK_DEPENDENCY_FAILURE":

                (
                    "Recommended remediation "
                    "includes dependency "
                    "verification, circuit "
                    "breaker activation, and "
                    "team escalation."
                ),

            "RUNBOOK_ROLLBACK":

                (
                    "Recommended remediation "
                    "includes deployment "
                    "rollback and release "
                    "validation."
                ),

            "RUNBOOK_NETWORK_RECOVERY":

                (
                    "Recommended remediation "
                    "includes DNS, ingress, "
                    "and network validation."
                ),

            "RUNBOOK_RESOURCE_SCALING":

                (
                    "Recommended remediation "
                    "includes scaling "
                    "deployment resources."
                )
        }

        return mapping.get(

            runbook,

            "Standard incident "
            "remediation recommended."
        )