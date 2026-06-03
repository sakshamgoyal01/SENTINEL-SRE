import logging

from ingestion.models.metric_event import MetricEvent


logger = logging.getLogger(
    "sentinel.processing.schema_validator"
)


def validate_metric_schema(
    event: MetricEvent
) -> bool:

    try:

        required_fields = [

            event.metric_name,

            event.service,

            event.value,

            event.timestamp

        ]

        if any(
            field is None
            for field in required_fields
        ):

            logger.warning(
                "Metric schema validation failed."
            )

            return False

        return True

    except Exception as e:

        logger.exception(
            f"Schema validation failed: {e}"
        )

        return False