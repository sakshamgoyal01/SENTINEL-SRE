from fastapi import APIRouter

# Intelligence
from backend.api.v1.intelligence.incidents import (
    router as incidents_router
)

from backend.api.v1.intelligence.investigations import (
    router as investigations_router
)

from backend.api.v1.intelligence.rootcauses import (
    router as rootcauses_router
)

from backend.api.v1.intelligence.risks import (
    router as risks_router
)

from backend.api.v1.intelligence.remediations import (
    router as remediations_router
)

from backend.api.v1.intelligence.knowledge import (
    router as knowledge_router
)

from backend.api.v1.intelligence.reports import (
    router as reports_router
)

from backend.api.v1.intelligence.aggregated_events import (
    router as aggregated_events_router
)

from backend.api.v1.intelligence.alerts import (
    router as alerts_router
)

# Operations
from backend.api.v1.operations.approvals import (
    router as approvals_router
)

from backend.api.v1.operations.executions import (
    router as executions_router
)

from backend.api.v1.operations.verifications import (
    router as verifications_router
)

from backend.api.v1.operations.recoveries import (
    router as recoveries_router
)

from backend.api.v1.operations.escalations import (
    router as escalations_router
)

from backend.api.v1.operations.states import (
    router as states_router
)

from backend.api.v1.operations.audits import (
    router as audits_router
)

# Telemetry
from backend.api.v1.telemetry.metrics import (
    router as metrics_router
)

from backend.api.v1.telemetry.logs import (
    router as logs_router
)

from backend.api.v1.telemetry.traces import (
    router as traces_router
)

from backend.api.v1.telemetry.kubernetes import (
    router as kubernetes_router
)

from backend.api.v1.telemetry.deployments import (
    router as deployments_router
)
from backend.api.v1.auth import (
    login_router,
    users_router,
    roles_router,
)
from backend.api.v1.telemetry.processed_telemetry import (
    router as processed_telemetry_router
)

# Platform
from backend.api.v1.system.dlq import (
    router as dlq_router
)

api_router = APIRouter()

# -------------------------
# Authentication
# -------------------------

api_router.include_router(
    login_router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(
    users_router,
    prefix="/auth/users",
    tags=["Users"],
)

api_router.include_router(
    roles_router,
    prefix="/auth/roles",
    tags=["Roles"],
)

# -------------------------
# Intelligence
# -------------------------

api_router.include_router(
    incidents_router,
    prefix="/incidents",
    tags=["Incidents"],
)

api_router.include_router(
    investigations_router,
    prefix="/investigations",
    tags=["Investigations"],
)

api_router.include_router(
    rootcauses_router,
    prefix="/rootcauses",
    tags=["Root Causes"],
)

api_router.include_router(
    risks_router,
    prefix="/risks",
    tags=["Risks"],
)

api_router.include_router(
    remediations_router,
    prefix="/remediations",
    tags=["Remediations"],
)

api_router.include_router(
    knowledge_router,
    prefix="/knowledge",
    tags=["Knowledge"],
)

api_router.include_router(
    reports_router,
    prefix="/reports",
    tags=["Reports"],
)

api_router.include_router(
    aggregated_events_router,
    prefix="/aggregated-events",
    tags=["Aggregated Events"],
)

api_router.include_router(
    alerts_router,
    prefix="/alerts",
    tags=["Alerts"],
)

# -------------------------
# Operations
# -------------------------

api_router.include_router(
    approvals_router,
    prefix="/approvals",
    tags=["Approvals"],
)

api_router.include_router(
    executions_router,
    prefix="/executions",
    tags=["Executions"],
)

api_router.include_router(
    verifications_router,
    prefix="/verifications",
    tags=["Verifications"],
)

api_router.include_router(
    recoveries_router,
    prefix="/recoveries",
    tags=["Recoveries"],
)

api_router.include_router(
    escalations_router,
    prefix="/escalations",
    tags=["Escalations"],
)

api_router.include_router(
    states_router,
    prefix="/states",
    tags=["Incident States"],
)

api_router.include_router(
    audits_router,
    prefix="/audits",
    tags=["Execution Audits"],
)

# -------------------------
# Telemetry
# -------------------------

api_router.include_router(
    metrics_router,
    prefix="/metrics",
    tags=["Metrics"],
)

api_router.include_router(
    logs_router,
    prefix="/logs",
    tags=["Logs"],
)

api_router.include_router(
    traces_router,
    prefix="/traces",
    tags=["Traces"],
)

api_router.include_router(
    kubernetes_router,
    prefix="/kubernetes",
    tags=["Kubernetes"],
)

api_router.include_router(
    deployments_router,
    prefix="/deployments",
    tags=["Deployments"],
)

api_router.include_router(
    processed_telemetry_router,
    prefix="/processed-telemetry",
    tags=["Processed Telemetry"],
)

# -------------------------
# Platform
# -------------------------

api_router.include_router(
    dlq_router,
    prefix="/dlq",
    tags=["Dead Letter Queue"],
)