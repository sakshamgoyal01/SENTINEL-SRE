import logging

from processing.classifiers.event_classifier import (
    EventClassifier
)

from processing.classifiers.operational_classifier import (
    OperationalClassifier
)

from processing.classifiers.severity_classifier import (
    SeverityClassifier
)

logger = logging.getLogger(
    "sentinel.classification.engine"
)


class ClassificationEngine:

    def __init__(self):

        self.event_classifier = (
            EventClassifier()
        )

        self.operational_classifier = (
            OperationalClassifier()
        )

        self.severity_classifier = (
            SeverityClassifier()
        )

    def classify(
        self,
        event
    ):

        event.event_family = (

            self.event_classifier.classify(
                event.category
            )
        )

        event.operational_type = (

            self.operational_classifier.classify(
                event
            )
        )

        event.severity = (

            self.severity_classifier.classify(
                event.severity
            )
        )

        return event