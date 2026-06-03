class IncidentSummarizer:

    def summarize(
        self,
        knowledge_record
    ) -> str:

        incident_type = (
            knowledge_record
            .pattern
            .incident_type
        )

        service = (
            knowledge_record
            .service
        )

        mapping = {

            "SERVICE_DEPENDENCY":
                (
                    f"{service} experienced "
                    f"a dependency-related "
                    f"production incident."
                ),

            "RELEASE_FAILURE":
                (
                    f"{service} experienced "
                    f"a deployment-related "
                    f"production incident."
                ),

            "NETWORK_OUTAGE":
                (
                    f"{service} experienced "
                    f"a network outage."
                ),

            "RESOURCE_CAPACITY":
                (
                    f"{service} experienced "
                    f"a resource capacity issue."
                )
        }

        return mapping.get(

            incident_type,

            f"{service} experienced "
            f"a production incident."
        )