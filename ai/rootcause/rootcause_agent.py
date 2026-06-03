import uuid

from datetime import datetime

from ai.models.root_cause import (
    RootCause
)

from ai.models.rootcause_result import (
    RootCauseResult
)

from ai.rootcause.evidence_analyzer import (
    EvidenceAnalyzer
)

from ai.rootcause.hypothesis_generator import (
    HypothesisGenerator
)

from ai.rootcause.rootcause_classifier import (
    RootCauseClassifier
)

from ai.rootcause.causal_chain_builder import (
    CausalChainBuilder
)

from ai.rootcause.confidence_estimator import (
    ConfidenceEstimator
)


class RootCauseAgent:

    def __init__(self):

        self.evidence_analyzer = (
            EvidenceAnalyzer()
        )

        self.hypothesis_generator = (
            HypothesisGenerator()
        )

        self.classifier = (
            RootCauseClassifier()
        )

        self.causal_chain_builder = (
            CausalChainBuilder()
        )

        self.confidence_estimator = (
            ConfidenceEstimator()
        )

    def analyze(
        self,
        investigation_result
    ) -> RootCauseResult:

        indicators = (

            self.evidence_analyzer
            .analyze(
                investigation_result
            )
        )

        hypotheses = (

            self.hypothesis_generator
            .generate(
                indicators
            )
        )

        (
            category,
            probable_cause
        ) = (

            self.classifier
            .classify(
                indicators
            )
        )

        confidence = (

            self.confidence_estimator
            .estimate(

                investigation_result,

                indicators
            )
        )

        root_cause = RootCause(

            category=category,

            probable_cause=(
                probable_cause
            ),

            confidence=confidence
        )

        causal_chain = (

            self.causal_chain_builder
            .build(
                category
            )
        )

        return RootCauseResult(

            rootcause_id=str(
                uuid.uuid4()
            ),

            investigation_id=(

                investigation_result
                .investigation_id
            ),

            service=(

                investigation_result
                .service
            ),

            severity=(

                investigation_result
                .severity
            ),

            priority=(

                investigation_result
                .priority
            ),

            root_cause=(
                root_cause
            ),

            causal_chain=(
                causal_chain
            ),

            evidence=(
                hypotheses
            ),

            confidence=(
                confidence
            ),

            generated_at=(
                datetime.utcnow()
            )
        )