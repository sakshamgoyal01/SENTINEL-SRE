import logging

from ingestion.models.metric_event import (
    MetricEvent
)

from processing.models.operational_event import (
    OperationalEvent
)

from processing.models.operational_context import (
    OperationalContext
)

from processing.models.processing_result import (
    ProcessingResult
)


logger = logging.getLogger(
    "sentinel.processing.metric_processor"
)


class MetricProcessor:

    CPU_WARNING = 70

    CPU_CRITICAL = 90

    MEMORY_WARNING = 75

    MEMORY_CRITICAL = 90

    ERROR_RATE_WARNING = 5

    ERROR_RATE_CRITICAL = 10

    def process(
        self,
        event: MetricEvent
    ) -> ProcessingResult:

        try:

            category = self._classify_metric(
                event.metric_name
            )

            severity = self._calculate_severity(
                event.metric_name,
                event.value
            )

            priority = self._calculate_priority(
                severity
            )

            risk_score = self._calculate_risk_score(
                event.value
            )

            summary = self._generate_summary(
                event.metric_name,
                event.value,
                severity
            )

            context = OperationalContext(

                service_type="application",

                dependencies=(
                    getattr(
                        event.metadata,
                        "dependencies",
                        []
                    )
                    if event.metadata
                    else []
                ),

                environment=(
                    event.metadata.environment
                ),

                cluster=(
                    event.metadata.cluster
                ),

                namespace=(
                    event.metadata.namespace
                ),

                team=(
                    event.metadata.team
                ),

                region=(
                    event.metadata.region
                )
            )

            operational_event = OperationalEvent(

                timestamp=event.timestamp,

                source=event.source,

                metadata=event.metadata,

                service=event.service,

                event_type="metric",

                category=category,

                severity=severity,

                priority=priority,

                risk_score=risk_score,

                summary=summary,

                operational_context=context,

                raw_event=event.model_dump()
            )

            return ProcessingResult(

                success=True,

                event=operational_event
            )

        except Exception as e:

            logger.exception(
                f"Metric processing failed: {e}"
            )

            return ProcessingResult(

                success=False,

                errors=[str(e)]
            )

    def _classify_metric(
        self,
        metric_name: str
    ) -> str:

        metric_name = metric_name.lower()

        if "cpu" in metric_name:

            return "performance"

        if "memory" in metric_name:

            return "performance"

        if "latency" in metric_name:

            return "availability"

        if "error" in metric_name:

            return "availability"

        return "observability"

    def _calculate_severity(
        self,
        metric_name: str,
        value: float
    ) -> str:

        metric_name = metric_name.lower()

        if "cpu" in metric_name:

            if value >= self.CPU_CRITICAL:
                return "CRITICAL"

            if value >= self.CPU_WARNING:
                return "WARNING"

        if "memory" in metric_name:

            if value >= self.MEMORY_CRITICAL:
                return "CRITICAL"

            if value >= self.MEMORY_WARNING:
                return "WARNING"

        if "error" in metric_name:

            if value >= self.ERROR_RATE_CRITICAL:
                return "CRITICAL"

            if value >= self.ERROR_RATE_WARNING:
                return "WARNING"

        return "INFO"

    def _calculate_priority(
        self,
        severity: str
    ) -> str:

        mapping = {

            "CRITICAL": "P1",

            "ERROR": "P2",

            "WARNING": "P3",

            "INFO": "P4"
        }

        return mapping.get(
            severity,
            "P4"
        )

    def _calculate_risk_score(
        self,
        value: float
    ) -> float:

        return min(
            round(float(value), 2),
            100.0
        )

    def _generate_summary(
        self,
        metric_name: str,
        value: float,
        severity: str
    ) -> str:

        return (
            f"{metric_name} "
            f"reported value {value} "
            f"with severity {severity}"
        )