import logging

from ingestion.models.log_event import LogEvent

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
    "sentinel.processing.log_processor"
)


class LogProcessor:

    def process(
        self,
        event: LogEvent
    ) -> ProcessingResult:

        try:

            category = self._classify_log(
                event.message
            )

            severity = self._calculate_severity(
                event
            )

            priority = self._calculate_priority(
                severity
            )

            risk_score = self._calculate_risk_score(
                severity
            )

            summary = self._generate_summary(
                event.message
            )

            context = OperationalContext(
                service_type="application",
                dependencies=[],
                environment=event.metadata.environment,
                cluster=event.metadata.cluster,
                namespace=event.metadata.namespace,
                team=event.metadata.team,
                region=event.metadata.region,
                correlated=(
                    event.trace_id is not None
                )
            )

            operational_event = OperationalEvent(
                timestamp=event.timestamp,
                source=event.source,
                metadata=event.metadata,
                service=event.service,
                event_type="log",
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
                f"Log processing failed: {e}"
            )

            return ProcessingResult(
                success=False,
                errors=[str(e)]
            )

    def _classify_log(
        self,
        message: str
    ) -> str:

        msg = message.lower()

        if "timeout" in msg:
            return "availability"

        if (
            "database" in msg
            or "postgres" in msg
            or "connection refused" in msg
        ):
            return "infrastructure"

        if (
            "unauthorized" in msg
            or "invalid token" in msg
            or "authentication failed" in msg
        ):
            return "security"

        return "application"

    def _calculate_severity(
        self,
        event: LogEvent
    ) -> str:

        return str(
            event.severity
        ).split(".")[-1]

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
        severity: str
    ) -> float:

        mapping = {
            "CRITICAL": 95.0,
            "ERROR": 75.0,
            "WARNING": 50.0,
            "INFO": 20.0
        }

        return mapping.get(
            severity,
            20.0
        )

    def _generate_summary(
        self,
        message: str
    ) -> str:

        return (
            message[:200]
            if len(message) > 200
            else message
        )