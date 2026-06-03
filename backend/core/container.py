from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.auth.user_repository import (
    UserRepository
)
from backend.repositories.auth.role_repository import (
    RoleRepository
)


from backend.repositories.auth.user_role_repository import (
    UserRoleRepository
)

from backend.services.auth.role_service import (
    RoleService
)

from backend.services.auth.user_service import (
    UserService
)
from backend.repositories.auth.user_role_repository import (
    UserRoleRepository
)

from backend.services.auth.role_service import (
    RoleService
)

from backend.services.auth.user_service import (
    UserService
)
from backend.services.auth.auth_service import (
    AuthService
)
from backend.persistence.handlers.deployment_handler import DeploymentPersistenceHandler
from backend.persistence.handlers.kubernetes_handler import KubernetesPersistenceHandler
from backend.persistence.handlers.log_handler import LogPersistenceHandler
from backend.persistence.handlers.metric_handler import MetricPersistenceHandler
from backend.persistence.handlers.trace_handler import TracePersistenceHandler
# ==========================================
# TELEMETRY REPOSITORIES
# ==========================================
from backend.repositories.telemetry.processed_telemetry_repository import (
    ProcessedTelemetryRepository
)

from backend.repositories.intelligence.aggregated_event_repository import (
    AggregatedEventRepository
)

from backend.repositories.intelligence.alert_repository import (
    AlertRepository
)

from backend.repositories.system.dead_letter_repository import (
    DeadLetterRepository
)
from backend.services.telemetry.processed_telemetry_service import (
    ProcessedTelemetryService
)

from backend.services.intelligence.aggregated_event_service import (
    AggregatedEventService
)

from backend.services.intelligence.alert_service import (
    AlertService
)

from backend.services.system.dead_letter_service import (
    DeadLetterService
)
from backend.persistence.handlers.processed_telemetry_handler import (
    ProcessedTelemetryPersistenceHandler
)

from backend.persistence.handlers.aggregated_event_handler import (
    AggregatedEventPersistenceHandler
)

from backend.persistence.handlers.alert_handler import (
    AlertPersistenceHandler
)

from backend.persistence.handlers.dead_letter_handler import (
    DeadLetterPersistenceHandler
)
from backend.repositories.telemetry.metric_repository import (
    MetricRepository
)

from backend.repositories.telemetry.log_repository import (
    LogRepository
)

from backend.repositories.telemetry.trace_repository import (
    TraceRepository
)

from backend.repositories.telemetry.kubernetes_repository import (
    KubernetesRepository
)

from backend.repositories.telemetry.deployment_repository import (
    DeploymentRepository
)

# ==========================================
# INTELLIGENCE REPOSITORIES
# ==========================================

from backend.repositories.intelligence.incident_repository import (
    IncidentRepository
)

from backend.repositories.intelligence.investigation_repository import (
    InvestigationRepository
)

from backend.repositories.intelligence.rootcause_repository import (
    RootCauseRepository
)

from backend.repositories.intelligence.risk_repository import (
    RiskRepository
)

from backend.repositories.intelligence.remediation_repository import (
    RemediationRepository
)

from backend.repositories.intelligence.knowledge_repository import (
    KnowledgeRepository
)

from backend.repositories.intelligence.executive_report_repository import (
    ExecutiveReportRepository
)

# ==========================================
# OPERATIONS REPOSITORIES
# ==========================================

from backend.repositories.Operations.approval_repository import (
    ApprovalRepository
)

from backend.repositories.Operations.execution_repository import (
    ExecutionRepository
)

from backend.repositories.Operations.verification_repository import (
    VerificationRepository
)

from backend.repositories.Operations.recovery_repository import (
    RecoveryRepository
)

from backend.repositories.Operations.escalation_repository import (
    EscalationRepository
)

from backend.repositories.Operations.execution_audit_repository import (
    ExecutionAuditRepository
)

from backend.repositories.Operations.incident_state_repository import (
    IncidentStateRepository
)

# ==========================================
# SERVICES
# ==========================================

from backend.services.intelligence.incident_service import (
    IncidentService
)

from backend.services.intelligence.investigation_service import (
    InvestigationService
)

from backend.services.intelligence.rootcause_service import (
    RootCauseService
)

from backend.services.intelligence.risk_service import (
    RiskService
)

from backend.services.intelligence.remediation_service import (
    RemediationService
)

from backend.services.intelligence.knowledge_service import (
    KnowledgeService
)

from backend.services.intelligence.executive_report_service import (
    ExecutiveReportService
)

from backend.services.operations.approval_service import (
    ApprovalService
)

from backend.services.operations.execution_service import (
    ExecutionService
)

from backend.services.operations.verification_service import (
    VerificationService
)

from backend.services.operations.recovery_service import (
    RecoveryService
)

from backend.services.operations.escalation_service import (
    EscalationService
)

from backend.services.operations.audit_service import (
    AuditService
)

from backend.services.operations.incident_state_service import (
    IncidentStateService
)

# ==========================================
# HANDLERS
# ==========================================

from backend.persistence.handlers.incident_handler import (
    IncidentPersistenceHandler
)

from backend.persistence.handlers.investigation_handler import (
    InvestigationPersistenceHandler
)

from backend.persistence.handlers.rootcause_handler import (
    RootCausePersistenceHandler
)

from backend.persistence.handlers.risk_handler import (
    RiskPersistenceHandler
)

from backend.persistence.handlers.remediation_handler import (
    RemediationPersistenceHandler
)

from backend.persistence.handlers.knowledge_handler import (
    KnowledgePersistenceHandler
)

from backend.persistence.handlers.executive_report_handler import (
    ExecutiveReportPersistenceHandler
)

from backend.persistence.handlers.approval_handler import (
    ApprovalPersistenceHandler
)

from backend.persistence.handlers.execution_handler import (
    ExecutionPersistenceHandler
)

from backend.persistence.handlers.verification_handler import (
    VerificationPersistenceHandler
)

from backend.persistence.handlers.recovery_handler import (
    RecoveryPersistenceHandler
)

from backend.persistence.handlers.escalation_handler import (
    EscalationPersistenceHandler
)

from backend.persistence.handlers.audit_handler import (
    AuditPersistenceHandler
)

from backend.persistence.handlers.incident_state_handler import (
    IncidentStatePersistenceHandler
)
from backend.services.telemetry.deployment_service import DeploymentService
from backend.services.telemetry.kubernetes_service import KubernetesService
from backend.services.telemetry.log_service import LogService
from backend.services.telemetry.metric_service import MetricService
from backend.services.telemetry.trace_service import TraceService


class Container:

    def __init__(
        self,
        session: AsyncSession,
    ):

        self.session = session

        # ==================================
        # INTELLIGENCE REPOSITORIES
        # ==================================

        self.incident_repository = (
            IncidentRepository(session)
        )
        self.user_repository = (
            UserRepository(session)
        )
        self.role_repository = (
            RoleRepository(session)
        )

        self.user_role_repository = (
            UserRoleRepository(session)
        )
        self.auth_service = (
            AuthService(
                self.user_repository
            )
        )
        self.user_service = (
            UserService(
                self.user_repository
            )
        )

        self.role_service = (
            RoleService(
                self.role_repository,
                self.user_role_repository,
            )
        )
        self.processed_telemetry_repository = (
            ProcessedTelemetryRepository(
                session
            )
        )
        self.role_repository = (
            RoleRepository(session)
        )

        self.user_role_repository = (
            UserRoleRepository(session)
        )
        self.user_service = (
            UserService(
                self.user_repository
            )
        )

        self.role_service = (
            RoleService(
                self.role_repository,
                self.user_role_repository,
            )
        )

        self.aggregated_event_repository = (
            AggregatedEventRepository(
                session
            )
        )

        self.alert_repository = (
            AlertRepository(
                session
            )
        )

        self.dead_letter_repository = (
            DeadLetterRepository(
                session
            )
        )
        self.metric_repository = (
            MetricRepository(session)
        )

        self.log_repository = (
            LogRepository(session)
        )

        self.trace_repository = (
            TraceRepository(session)
        )

        self.kubernetes_repository = (
            KubernetesRepository(session)
        )

        self.deployment_repository = (
            DeploymentRepository(session)
        )

        self.investigation_repository = (
            InvestigationRepository(session)
        )

        self.rootcause_repository = (
            RootCauseRepository(session)
        )

        self.risk_repository = (
            RiskRepository(session)
        )

        self.remediation_repository = (
            RemediationRepository(session)
        )

        self.knowledge_repository = (
            KnowledgeRepository(session)
        )

        self.executive_report_repository = (
            ExecutiveReportRepository(session)
        )

        # ==================================
        # OPERATIONS REPOSITORIES
        # ==================================

        self.approval_repository = (
            ApprovalRepository(session)
        )

        self.execution_repository = (
            ExecutionRepository(session)
        )

        self.verification_repository = (
            VerificationRepository(session)
        )

        self.recovery_repository = (
            RecoveryRepository(session)
        )

        self.escalation_repository = (
            EscalationRepository(session)
        )

        self.audit_repository = (
            ExecutionAuditRepository(session)
        )

        self.incident_state_repository = (
            IncidentStateRepository(session)
        )

        # ==================================
        # SERVICES
        # ==================================

        self.incident_service = (
            IncidentService(
                self.incident_repository
            )
        )
        self.processed_telemetry_service = (
            ProcessedTelemetryService(
                self.processed_telemetry_repository
            )
        )

        self.aggregated_event_service = (
            AggregatedEventService(
                self.aggregated_event_repository
            )
        )

        self.alert_service = (
            AlertService(
                self.alert_repository
            )
        )

        self.dead_letter_service = (
            DeadLetterService(
                self.dead_letter_repository
            )
        )
        self.metric_service = (
            MetricService(
                self.metric_repository
            )
        )

        self.log_service = (
            LogService(
                self.log_repository
            )
        )

        self.trace_service = (
            TraceService(
                self.trace_repository
            )
        )

        self.kubernetes_service = (
            KubernetesService(
                self.kubernetes_repository
            )
        )

        self.deployment_service = (
            DeploymentService(
                self.deployment_repository
            )
        )

        self.investigation_service = (
            InvestigationService(
                self.investigation_repository
            )
        )

        self.rootcause_service = (
            RootCauseService(
                self.rootcause_repository
            )
        )

        self.risk_service = (
            RiskService(
                self.risk_repository
            )
        )

        self.remediation_service = (
            RemediationService(
                self.remediation_repository
            )
        )

        self.knowledge_service = (
            KnowledgeService(
                self.knowledge_repository
            )
        )

        self.executive_report_service = (
            ExecutiveReportService(
                self.executive_report_repository
            )
        )

        self.approval_service = (
            ApprovalService(
                self.approval_repository
            )
        )

        self.execution_service = (
            ExecutionService(
                self.execution_repository
            )
        )

        self.verification_service = (
            VerificationService(
                self.verification_repository
            )
        )

        self.recovery_service = (
            RecoveryService(
                self.recovery_repository
            )
        )

        self.escalation_service = (
            EscalationService(
                self.escalation_repository
            )
        )

        self.audit_service = (
            AuditService(
                self.audit_repository
            )
        )

        self.incident_state_service = (
            IncidentStateService(
                self.incident_state_repository
            )
        )

        # ==================================
        # HANDLERS
        # ==================================

        self.incident_handler = (
            IncidentPersistenceHandler(
                self.incident_service
            )
        )
        self.metric_handler = (
            MetricPersistenceHandler(
                self.metric_service
            )
        )


        self.log_handler = (
            LogPersistenceHandler(
                self.log_service
            )
        )

        self.trace_handler = (
            TracePersistenceHandler(
                self.trace_service
            )
        )

        self.kubernetes_handler = (
            KubernetesPersistenceHandler(
                self.kubernetes_service
            )
        )

        self.deployment_handler = (
            DeploymentPersistenceHandler(
                self.deployment_service
            )
        )

        self.investigation_handler = (
            InvestigationPersistenceHandler(
                self.investigation_service
            )
        )

        self.rootcause_handler = (
            RootCausePersistenceHandler(
                self.rootcause_service
            )
        )

        self.risk_handler = (
            RiskPersistenceHandler(
                self.risk_service
            )
        )
        self.processed_telemetry_handler = (
            ProcessedTelemetryPersistenceHandler(
                self.processed_telemetry_service
            )
        )

        self.aggregated_event_handler = (
            AggregatedEventPersistenceHandler(
                self.aggregated_event_service
            )
        )

        self.alert_handler = (
            AlertPersistenceHandler(
                self.alert_service
            )
        )

        self.dead_letter_handler = (
            DeadLetterPersistenceHandler(
                self.dead_letter_service
            )
        )

        self.remediation_handler = (
            RemediationPersistenceHandler(
                self.remediation_service
            )
        )

        self.knowledge_handler = (
            KnowledgePersistenceHandler(
                self.knowledge_service
            )
        )

        self.executive_report_handler = (
            ExecutiveReportPersistenceHandler(
                self.executive_report_service
            )
        )

        self.approval_handler = (
            ApprovalPersistenceHandler(
                self.approval_service
            )
        )

        self.execution_handler = (
            ExecutionPersistenceHandler(
                self.execution_service
            )
        )

        self.verification_handler = (
            VerificationPersistenceHandler(
                self.verification_service
            )
        )

        self.recovery_handler = (
            RecoveryPersistenceHandler(
                self.recovery_service
            )
        )

        self.escalation_handler = (
            EscalationPersistenceHandler(
                self.escalation_service
            )
        )

        self.audit_handler = (
            AuditPersistenceHandler(
                self.audit_service
            )
        )

        self.incident_state_handler = (
            IncidentStatePersistenceHandler(
                self.incident_state_service
            )
        )

    def get_handler_instances(
        self,
    ) -> dict:

        from backend.persistence.handlers.incident_handler import (
            IncidentPersistenceHandler
        )

        from backend.persistence.handlers.investigation_handler import (
            InvestigationPersistenceHandler
        )

        from backend.persistence.handlers.rootcause_handler import (
            RootCausePersistenceHandler
        )

        from backend.persistence.handlers.risk_handler import (
            RiskPersistenceHandler
        )

        from backend.persistence.handlers.remediation_handler import (
            RemediationPersistenceHandler
        )

        from backend.persistence.handlers.knowledge_handler import (
            KnowledgePersistenceHandler
        )

        from backend.persistence.handlers.executive_report_handler import (
            ExecutiveReportPersistenceHandler
        )

        from backend.persistence.handlers.approval_handler import (
            ApprovalPersistenceHandler
        )

        from backend.persistence.handlers.execution_handler import (
            ExecutionPersistenceHandler
        )

        from backend.persistence.handlers.verification_handler import (
            VerificationPersistenceHandler
        )

        from backend.persistence.handlers.recovery_handler import (
            RecoveryPersistenceHandler
        )

        from backend.persistence.handlers.escalation_handler import (
            EscalationPersistenceHandler
        )

        from backend.persistence.handlers.audit_handler import (
            AuditPersistenceHandler
        )

        from backend.persistence.handlers.incident_state_handler import (
            IncidentStatePersistenceHandler
        )

        return {

            IncidentPersistenceHandler:
                self.incident_handler,
            MetricPersistenceHandler:
                self.metric_handler,

            LogPersistenceHandler:
                self.log_handler,

            TracePersistenceHandler:
                self.trace_handler,
            ProcessedTelemetryPersistenceHandler:
                self.processed_telemetry_handler,

            AggregatedEventPersistenceHandler:
                self.aggregated_event_handler,

            AlertPersistenceHandler:
                self.alert_handler,

            DeadLetterPersistenceHandler:
                self.dead_letter_handler,

            KubernetesPersistenceHandler:
                self.kubernetes_handler,

            DeploymentPersistenceHandler:
                self.deployment_handler,

            InvestigationPersistenceHandler:
                self.investigation_handler,

            RootCausePersistenceHandler:
                self.rootcause_handler,

            RiskPersistenceHandler:
                self.risk_handler,

            RemediationPersistenceHandler:
                self.remediation_handler,

            KnowledgePersistenceHandler:
                self.knowledge_handler,

            ExecutiveReportPersistenceHandler:
                self.executive_report_handler,

            ApprovalPersistenceHandler:
                self.approval_handler,

            ExecutionPersistenceHandler:
                self.execution_handler,

            VerificationPersistenceHandler:
                self.verification_handler,

            RecoveryPersistenceHandler:
                self.recovery_handler,

            EscalationPersistenceHandler:
                self.escalation_handler,

            AuditPersistenceHandler:
                self.audit_handler,

            IncidentStatePersistenceHandler:
                self.incident_state_handler,
        }
