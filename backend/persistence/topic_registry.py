from backend.persistence.handlers.incident_handler import (
    IncidentPersistenceHandler
)
from backend.persistence.handlers.metric_handler import (
    MetricPersistenceHandler
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
from backend.persistence.handlers.log_handler import (
    LogPersistenceHandler
)

from backend.persistence.handlers.trace_handler import (
    TracePersistenceHandler
)

from backend.persistence.handlers.kubernetes_handler import (
    KubernetesPersistenceHandler
)

from backend.persistence.handlers.deployment_handler import (
    DeploymentPersistenceHandler
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
TOPIC_HANDLERS = {
"sentinel.processed.telemetry":
    ProcessedTelemetryPersistenceHandler,

"sentinel.aggregated.events":
    AggregatedEventPersistenceHandler,

"sentinel.alerts":
    AlertPersistenceHandler,

"sentinel.dlq":
    DeadLetterPersistenceHandler,
    "sentinel.metrics":
        MetricPersistenceHandler,

    "sentinel.logs":
        LogPersistenceHandler,

    "sentinel.traces":
        TracePersistenceHandler,

    "sentinel.k8s.events":
        KubernetesPersistenceHandler,

    "sentinel.deployments":
        DeploymentPersistenceHandler,

    "sentinel.incidents":
        IncidentPersistenceHandler,

    "sentinel.investigation.results":
        InvestigationPersistenceHandler,

    "sentinel.rootcause.results":
        RootCausePersistenceHandler,

    "sentinel.risk.results":
        RiskPersistenceHandler,

    "sentinel.remediation.results":
        RemediationPersistenceHandler,

    "sentinel.knowledge.records":
        KnowledgePersistenceHandler,

    "sentinel.executive.summaries":
        ExecutiveReportPersistenceHandler,

    "sentinel.approved.actions":
        ApprovalPersistenceHandler,

    "sentinel.execution.results":
        ExecutionPersistenceHandler,

    "sentinel.verification.results":
        VerificationPersistenceHandler,

    "sentinel.recovery.results":
        RecoveryPersistenceHandler,

    "sentinel.escalations":
        EscalationPersistenceHandler,

    "sentinel.execution.audit":
        AuditPersistenceHandler,

    "sentinel.incident.state":
        IncidentStatePersistenceHandler,
}