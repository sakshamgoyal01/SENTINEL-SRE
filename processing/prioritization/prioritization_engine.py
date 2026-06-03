from processing.models.prioritized_event import (
    PrioritizedEvent
)

from processing.prioritization.impact_estimator import (
    ImpactEstimator
)

from processing.prioritization.risk_score_calculator import (
    RiskScoreCalculator
)

from processing.prioritization.priority_calculator import (
    PriorityCalculator
)


class PrioritizationEngine:

    def __init__(self):

        self.impact_estimator = (
            ImpactEstimator()
        )

        self.risk_calculator = (
            RiskScoreCalculator()
        )

        self.priority_calculator = (
            PriorityCalculator()
        )

    def prioritize(
        self,
        aggregated_event
    ) -> PrioritizedEvent:

        impact_score = (

            self.impact_estimator
            .estimate(
                aggregated_event
            )
        )

        final_risk = (

            self.risk_calculator
            .calculate(
                aggregated_event,
                impact_score
            )
        )

        priority = (

            self.priority_calculator
            .calculate(
                final_risk
            )
        )

        requires_review = (
            priority == "P1"
        )

        escalation_required = (
            priority in [
                "P1",
                "P2"
            ]
        )

        return PrioritizedEvent(

            incident_priority=priority,

            impact_score=impact_score,

            final_risk_score=final_risk,

            requires_human_review=(
                requires_review
            ),

            escalation_required=(
                escalation_required
            ),

            aggregated_event=(
                aggregated_event
            )
        )