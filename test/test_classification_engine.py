from datetime import datetime

from ingestion.models.metadata import Metadata

from processing.classifiers.classification_engine import (
    ClassificationEngine
)

from processing.models.operational_event import (
    OperationalEvent
)

from processing.models.operational_context import (
    OperationalContext
)


def test_classification_engine():

    metadata = Metadata(

        cluster="local",

        namespace="default",

        environment="dev",

        team="backend",

        region="local"
    )

    event = OperationalEvent(

        timestamp=datetime.utcnow(),

        source="loki",

        metadata=metadata,

        service="payment-service",

        event_type="log",

        category="availability",

        severity="CRITICAL",

        priority="P1",

        risk_score=95,

        summary="Database timeout",

        operational_context=(

            OperationalContext(

                environment="dev",

                cluster="local",

                namespace="default"
            )
        ),

        raw_event={}
    )

    engine = ClassificationEngine()

    result = engine.classify(
        event
    )

    assert (
        result.event_family
        == "reliability"
    )

    assert (
        result.operational_type
        == "dependency_failure"
    )