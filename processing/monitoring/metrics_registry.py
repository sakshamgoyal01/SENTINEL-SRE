from prometheus_client import (
    Counter,
    Gauge,
    Histogram
)

EVENTS_PROCESSED = Counter(

    "sentinel_events_processed_total",

    "Total processed events"
)

EVENTS_AGGREGATED = Counter(

    "sentinel_events_aggregated_total",

    "Total aggregated events"
)

EVENTS_PRIORITIZED = Counter(

    "sentinel_events_prioritized_total",

    "Total prioritized events"
)

EVENTS_ROUTED = Counter(

    "sentinel_events_routed_total",

    "Total routed events"
)

PROCESSING_FAILURES = Counter(

    "sentinel_processing_failures_total",

    "Processing failures"
)

VALIDATION_FAILURES = Counter(

    "sentinel_validation_failures_total",

    "Validation failures"
)

PROCESSING_LATENCY = Histogram(

    "sentinel_processing_latency_seconds",

    "Processing latency"
)

CONSUMER_LAG = Gauge(

    "sentinel_consumer_lag",

    "Kafka consumer lag"
)