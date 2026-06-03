import logging
import time
from ingestion.models.metric_event import (
    MetricEvent
)

from ingestion.models.log_event import (
    LogEvent
)
from processing.aggregation.aggregation_manager import (
    AggregationManager
)
from processing.prioritization.prioritization_engine import (
    PrioritizationEngine
)

from processing.routing.routing_manager import (
    RoutingManager
)
from processing.publishers.aggregated_event_publisher import (
    AggregatedEventPublisher
)
from ingestion.models.trace_event import (
    TraceEvent
)

from ingestion.models.deployment_event import (
    DeploymentEvent
)

from ingestion.models.kubernetes_event import (
    KubernetesEvent
)

from processing.classifiers.classification_engine import (
    ClassificationEngine
)

from processing.processors.metric_processor import (
    MetricProcessor
)

from processing.processors.log_processor import (
    LogProcessor
)

from processing.processors.trace_processor import (
    TraceProcessor
)

from processing.processors.deployment_processor import (
    DeploymentProcessor
)

from processing.processors.k8s_processor import (
    KubernetesProcessor
)

from processing.validators.schema_validator import (
    validate_metric_schema
)

from processing.validators.telemetry_validator import (
    validate_metric_quality
)

from processing.publishers.processed_event_publisher import (
    ProcessedEventPublisher
)


logger = logging.getLogger(
    "sentinel.processing.pipeline"
)


class ProcessingPipeline:

    def __init__(self):

        self.processor = MetricProcessor()

        self.log_processor = (
            LogProcessor()
        )

        self.trace_processor = (
            TraceProcessor()
        )

        self.deployment_processor = (
            DeploymentProcessor()
        )

        self.k8s_processor = (
            KubernetesProcessor()
        )

        self.classification_engine = (
            ClassificationEngine()
        )
        self.aggregation_manager = (
            AggregationManager()
        )

        self.aggregated_publisher = (
            AggregatedEventPublisher()
        )
        self.prioritization_engine = (
            PrioritizationEngine()
        )

        self.routing_manager = (
            RoutingManager()
        )

        self.publisher = (
            ProcessedEventPublisher()
        )

    def _publish_processed_event(
            self,
            result
    ):

        classified_event = (
            self.classification_engine.classify(
                result.event
            )
        )

        aggregation_result = (
            self.aggregation_manager.aggregate(
                classified_event
            )
        )

        if (
                aggregation_result
                and
                aggregation_result.triggered
        ):
            self.aggregated_publisher.publish(
                aggregation_result.aggregated_event
            )

            prioritized_event = (
                self.prioritization_engine.prioritize(
                    aggregation_result.aggregated_event
                )
            )

            self.routing_manager.route(
                prioritized_event
            )

        return self.publisher.publish(
            classified_event
        )

    def process_metric(
        self,
        event: MetricEvent
    ):

        if not validate_metric_schema(
            event
        ):

            logger.warning(
                "Schema validation failed."
            )

            return False

        if not validate_metric_quality(
            event
        ):

            logger.warning(
                "Telemetry validation failed."
            )

            return False

        result = self.processor.process(
            event
        )

        if not result.success:

            logger.warning(
                f"Processing failed: "
                f"{result.errors}"
            )

            return False

        return self._publish_processed_event(
            result
        )

    def process_log(
        self,
        event: LogEvent
    ):

        result = (
            self.log_processor.process(
                event
            )
        )

        if not result.success:

            logger.warning(
                f"Log processing failed: "
                f"{result.errors}"
            )

            return False

        return self._publish_processed_event(
            result
        )

    def process_trace(
        self,
        event: TraceEvent
    ):

        result = (
            self.trace_processor.process(
                event
            )
        )

        if not result.success:

            logger.warning(
                f"Trace processing failed: "
                f"{result.errors}"
            )

            return False

        return self._publish_processed_event(
            result
        )

    def process_deployment(
        self,
        event: DeploymentEvent
    ):

        result = (
            self.deployment_processor.process(
                event
            )
        )

        if not result.success:

            logger.warning(
                f"Deployment processing failed: "
                f"{result.errors}"
            )

            return False

        return self._publish_processed_event(
            result
        )

    def process_k8s(
        self,
        event: KubernetesEvent
    ):

        result = (
            self.k8s_processor.process(
                event
            )
        )

        if not result.success:

            logger.warning(
                f"Kubernetes event processing failed: "
                f"{result.errors}"
            )

            return False

        return self._publish_processed_event(
            result
        )