import uuid

from datetime import datetime

from ai.models.audit_record import (
    AuditRecord
)


class AuditBuilder:

    def build_from_recovery(
        self,
        recovery_result
    ) -> AuditRecord:

        return AuditRecord(

            audit_id=str(
                uuid.uuid4()
            ),

            service=(
                recovery_result
                .service
            ),

            approval_id=None,

            execution_id=None,

            verification_id=(
                recovery_result
                .verification_id
            ),

            recovery_id=(
                recovery_result
                .recovery_id
            ),

            status=(
                recovery_result
                .recovery_status
            ),

            details=(
                recovery_result
                .strategy
                .strategy_type
            ),

            created_at=(
                datetime.utcnow()
            )
        )