from typing import TypedDict, Optional


class MetricEventSchema(TypedDict):

    service: str

    metric_name: str

    value: float

    timestamp: str

    labels: dict


class LogEventSchema(TypedDict):

    service: str

    severity: str

    message: str

    timestamp: str

    trace_id: Optional[str]


class TraceEventSchema(TypedDict):

    trace_id: str

    service: str

    operation: str

    duration_ms: float

    timestamp: str


class IncidentEventSchema(TypedDict):

    incident_id: str

    service: str

    severity: str

    description: str

    timestamp: str


class DeploymentEventSchema(TypedDict):

    deployment_name: str

    namespace: str

    replicas: int

    available_replicas: int

    updated_replicas: int

    creation_timestamp: str

    labels: dict

class BaseEventSchema(TypedDict):

    event_id: str

    timestamp: str

    source: str

    version: str