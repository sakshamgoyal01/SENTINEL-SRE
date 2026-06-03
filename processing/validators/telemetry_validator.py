import logging

from ingestion.models.metric_event import (
    MetricEvent
)


logger = logging.getLogger(
    "sentinel.processing.telemetry_validator"
)


INVALID_SERVICES = {

    "unknown-service",
    "",
    None
}


INVALID_METRICS = {

    "unknown_metric",
    "",
    None
}


def validate_metric_quality(
    event: MetricEvent
) -> bool:

    try:

        if event.service in INVALID_SERVICES:

            logger.warning(
                "Invalid service detected."
            )

            return False

        if event.metric_name in INVALID_METRICS:

            logger.warning(
                "Invalid metric detected."
            )

            return False

        if event.value is None:

            logger.warning(
                "Metric value missing."
            )

            return False

        return True

    except Exception as e:

        logger.exception(
            f"Telemetry validation failed: {e}"
        )

        return False