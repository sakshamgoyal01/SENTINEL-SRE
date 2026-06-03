from processing.monitoring.metrics_registry import (

    EVENTS_PROCESSED,

    EVENTS_AGGREGATED,

    EVENTS_PRIORITIZED,

    EVENTS_ROUTED,

    PROCESSING_FAILURES,

    VALIDATION_FAILURES
)


class ProcessingMetrics:

    @staticmethod
    def processed():

        EVENTS_PROCESSED.inc()

    @staticmethod
    def aggregated():

        EVENTS_AGGREGATED.inc()

    @staticmethod
    def prioritized():

        EVENTS_PRIORITIZED.inc()

    @staticmethod
    def routed():

        EVENTS_ROUTED.inc()

    @staticmethod
    def processing_failure():

        PROCESSING_FAILURES.inc()

    @staticmethod
    def validation_failure():

        VALIDATION_FAILURES.inc()