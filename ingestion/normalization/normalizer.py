from ingestion.normalization.timestamp_normalizer import (
    normalize_timestamp
)

from ingestion.normalization.severity_mapper import (
    normalize_severity
)

from ingestion.normalization.service_mapper import (
    normalize_service
)

from ingestion.normalization.metadata_enricher import (
    enrich_metadata
)

from ingestion.normalization.topology_enricher import (
    enrich_topology
)

from ingestion.normalization.trace_correlator import (
    correlate_trace
)

from ingestion.normalization.deduplicator import (
    is_duplicate
)


def normalize_event(event: dict):

    if "timestamp" in event:

        event["timestamp"] = normalize_timestamp(
            event["timestamp"]
        )

    if "severity" in event:

        event["severity"] = normalize_severity(
            event["severity"]
        )

    if "service" in event:

        event["service"] = normalize_service(
            event["service"]
        )

    event = enrich_metadata(event)

    event = enrich_topology(event)

    event = correlate_trace(event)

    if is_duplicate(event):

        return None

    return event