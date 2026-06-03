from ai.knowledge.incident_normalizer import (
    IncidentNormalizer
)

from ai.knowledge.remediation_tracker import (
    RemediationTracker
)

from ai.knowledge.incident_classifier import (
    IncidentClassifier
)

from ai.knowledge.knowledge_builder import (
    KnowledgeBuilder
)


class KnowledgeAgent:

    def __init__(self):

        self.normalizer = (
            IncidentNormalizer()
        )

        self.tracker = (
            RemediationTracker()
        )

        self.classifier = (
            IncidentClassifier()
        )

        self.builder = (
            KnowledgeBuilder()
        )

    def analyze(
        self,
        remediation_result
    ):

        normalized_type = (

            self.normalizer
            .normalize(

                remediation_result
                .plan
                .runbook
            )
        )

        incident_type = (

            self.classifier
            .classify(
                normalized_type
            )
        )

        remediation_outcome = (

            self.tracker
            .extract(
                remediation_result
            )
        )

        return (

            self.builder
            .build(

                remediation_result,

                incident_type,

                normalized_type,

                remediation_outcome
            )
        )