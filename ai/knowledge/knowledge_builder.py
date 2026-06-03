import uuid

from datetime import datetime

from ai.models.incident_pattern import (
    IncidentPattern
)

from ai.models.knowledge_record import (
    KnowledgeRecord
)


class KnowledgeBuilder:

    def build(

        self,

        remediation_result,

        incident_type: str,

        normalized_type: str,

        remediation_outcome
    ) -> KnowledgeRecord:

        pattern = IncidentPattern(

            incident_type=(
                incident_type
            ),

            service=(
                remediation_result
                .service
            ),

            severity=(
                remediation_result
                .priority
            ),

            root_cause=(
                normalized_type
            )
        )

        return KnowledgeRecord(

            knowledge_id=str(
                uuid.uuid4()
            ),

            service=(
                remediation_result
                .service
            ),

            pattern=pattern,

            remediation=(
                remediation_outcome
            ),

            created_at=(
                datetime.utcnow()
            )
        )