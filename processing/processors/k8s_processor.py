import logging

from ingestion.models.kubernetes_event import (
    KubernetesEvent
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
    "sentinel.processing.k8s_processor"
)


class KubernetesProcessor:

    def process(
        self,
        event: KubernetesEvent
    ) -> ProcessingResult:

        try:

            category = self._classify_event(
                event
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
                event
            )

            object_name = (
                event.involved_object.get(
                    "name",
                    "unknown"
                )
            )

            context = OperationalContext(

                service_type="kubernetes",

                dependencies=[],

                environment=(
                    event.metadata.environment
                ),

                cluster=(
                    event.metadata.cluster
                ),

                namespace=(
                    event.metadata.namespace
                ),

                resource_type=(
                    event.involved_object.get(
                        "kind"
                    )
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

                service=object_name,

                event_type="k8s_event",

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
                f"K8s processing failed: {e}"
            )

            return ProcessingResult(
                success=False,
                errors=[str(e)]
            )

    def _classify_event(
        self,
        event: KubernetesEvent
    ) -> str:

        reason = event.reason.lower()

        if (
            "crashloopbackoff" in reason
            or "oomkilled" in reason
        ):
            return "availability"

        if (
            "failedscheduling" in reason
        ):
            return "infrastructure"

        if (
            "imagepullbackoff" in reason
        ):
            return "deployment"

        return "kubernetes"

    def _calculate_severity(
        self,
        event: KubernetesEvent
    ) -> str:

        reason = event.reason.lower()

        critical_events = {

            "crashloopbackoff",

            "oomkilled",

            "node not ready",

            "failedmount"
        }

        warning_events = {

            "failedscheduling",

            "imagepullbackoff",

            "backoff"
        }

        if reason in critical_events:
            return "CRITICAL"

        if reason in warning_events:
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
        severity: str
    ) -> float:

        mapping = {

            "CRITICAL": 95.0,

            "WARNING": 60.0,

            "INFO": 20.0
        }

        return mapping.get(
            severity,
            20.0
        )

    def _generate_summary(
        self,
        event: KubernetesEvent
    ) -> str:

        return (
            f"{event.reason}: "
            f"{event.message}"
        )