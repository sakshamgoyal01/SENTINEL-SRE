import uuid
from datetime import datetime

from ai.models.investigation_result import (
    InvestigationResult
)

from ai.investigation.evidence_extractor import (
    EvidenceExtractor
)

from ai.investigation.timeline_builder import (
    TimelineBuilder
)

from ai.investigation.signal_correlator import (
    SignalCorrelator
)

from ai.investigation.confidence_calculator import (
    ConfidenceCalculator
)


class InvestigationAgent:

    def __init__(self):

        self.extractor = (
            EvidenceExtractor()
        )

        self.timeline_builder = (
            TimelineBuilder()
        )

        self.correlator = (
            SignalCorrelator()
        )

        self.confidence = (
            ConfidenceCalculator()
        )

    def investigate(
        self,
        prioritized_event
    ):

        event = (
            prioritized_event
            .aggregated_event
        )

        return InvestigationResult(

            investigation_id=str(
                uuid.uuid4()
            ),

            service=event.services[0],

            severity=event.severity,

            priority=(
                prioritized_event
                .incident_priority
            ),

            summary=event.summary,

            findings=(
                self.correlator
                .correlate(
                    prioritized_event
                )
            ),

            evidence=(
                self.extractor
                .extract(
                    prioritized_event
                )
            ),

            timeline=(
                self.timeline_builder
                .build(
                    prioritized_event
                )
            ),

            confidence=(
                self.confidence
                .calculate(
                    prioritized_event
                )
            ),

            generated_at=(
                datetime.utcnow()
            )
        )