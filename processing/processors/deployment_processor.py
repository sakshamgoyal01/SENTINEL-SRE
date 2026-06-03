import logging

from ingestion.models.deployment_event import (
    DeploymentEvent
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
    "sentinel.processing.deployment_processor"
)


class DeploymentProcessor:

    def process(
        self,
        event: DeploymentEvent
    ) -> ProcessingResult:

        try:

            category = self._classify_deployment(
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

                service_type="deployment",

                dependencies=[],

                environment=(
                    event.metadata.environment
                ),

                cluster=(
                    event.metadata.cluster
                ),

                namespace=(
                    event.namespace
                ),

                deployment_name=(
                    event.deployment_name
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

                service=event.deployment_name,

                event_type="deployment",

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
                f"Deployment processing failed: {e}"
            )

            return ProcessingResult(
                success=False,
                errors=[str(e)]
            )

    def _classify_deployment(
        self,
        event: DeploymentEvent
    ) -> str:

        if (
            event.available_replicas is not None
            and
            event.available_replicas
            < event.replicas
        ):
            return "deployment"

        return "release"

    def _calculate_severity(
        self,
        event: DeploymentEvent
    ) -> str:

        available = (
            event.available_replicas
            or 0
        )

        if available == 0:
            return "CRITICAL"

        if available < event.replicas:
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
        event: DeploymentEvent
    ) -> float:

        available = (
            event.available_replicas
            or 0
        )

        if event.replicas == 0:
            return 100.0

        unavailable = (
            event.replicas
            - available
        )

        score = (
            unavailable
            / event.replicas
        ) * 100

        return round(score, 2)

    def _generate_summary(
        self,
        event: DeploymentEvent
    ) -> str:

        available = (
            event.available_replicas
            or 0
        )

        return (
            f"Deployment "
            f"{event.deployment_name} "
            f"has "
            f"{available}/{event.replicas} "
            f"available replicas"
        )