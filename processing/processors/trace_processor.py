import logging

from ingestion.models.trace_event import TraceEvent

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
    "sentinel.processing.trace_processor"
)


class TraceProcessor:

    LATENCY_WARNING = 500

    LATENCY_CRITICAL = 1000

    def process(
        self,
        event: TraceEvent
    ) -> ProcessingResult:

        try:

            category = self._classify_trace(
                event
            )

            severity = self._calculate_severity(
                event
            )

            priority = self._calculate_priority(
                severity
            )

            risk_score = self._calculate_risk_score(
                event
            )

            summary = self._generate_summary(
                event
            )

            context = OperationalContext(

                service_type="application",

                dependencies=[],

                environment=event.metadata.environment,

                cluster=event.metadata.cluster,

                namespace=event.metadata.namespace,

                team=event.metadata.team,

                region=event.metadata.region,

                correlated=True
            )

            operational_event = OperationalEvent(

                timestamp=event.timestamp,

                source=event.source,

                metadata=event.metadata,

                service=event.service,

                event_type="trace",

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
                f"Trace processing failed: {e}"
            )

            return ProcessingResult(
                success=False,
                errors=[str(e)]
            )

    def _classify_trace(
        self,
        event: TraceEvent
    ) -> str:

        if event.status_code:

            if event.status_code >= 500:
                return "availability"

            if event.status_code >= 400:
                return "application"

        if (
            event.duration_ms
            > self.LATENCY_WARNING
        ):
            return "performance"

        return "observability"

    def _calculate_severity(
        self,
        event: TraceEvent
    ) -> str:

        if event.status_code:

            if event.status_code >= 500:
                return "CRITICAL"

            if event.status_code >= 400:
                return "WARNING"

        if (
            event.duration_ms
            >= self.LATENCY_CRITICAL
        ):
            return "CRITICAL"

        if (
            event.duration_ms
            >= self.LATENCY_WARNING
        ):
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
        event: TraceEvent
    ) -> float:

        score = min(
            event.duration_ms / 10,
            100
        )

        if (
            event.status_code
            and event.status_code >= 500
        ):
            score = 100

        return round(score, 2)

    def _generate_summary(
        self,
        event: TraceEvent
    ) -> str:

        if (
            event.status_code
            and event.status_code >= 500
        ):

            return (
                f"{event.service} "
                f"operation "
                f"{event.operation} "
                f"failed with "
                f"status {event.status_code}"
            )

        return (
            f"{event.service} "
            f"operation "
            f"{event.operation} "
            f"executed in "
            f"{event.duration_ms}ms"
        )