import uuid

from datetime import datetime

from ai.models.impact_assessment import (
    ImpactAssessment
)

from ai.models.risk_summary import (
    RiskSummary
)

from ai.models.risk_result import (
    RiskResult
)

from ai.risk.blast_radius_calculator import (
    BlastRadiusCalculator
)

from ai.risk.customer_impact_estimator import (
    CustomerImpactEstimator
)

from ai.risk.business_impact_estimator import (
    BusinessImpactEstimator
)

from ai.risk.slo_risk_calculator import (
    SloRiskCalculator
)

from ai.risk.mttr_predictor import (
    MttrPredictor
)


class RiskAgent:

    def __init__(self):

        self.blast_radius = (
            BlastRadiusCalculator()
        )

        self.customer_impact = (
            CustomerImpactEstimator()
        )

        self.business_impact = (
            BusinessImpactEstimator()
        )

        self.slo_risk = (
            SloRiskCalculator()
        )

        self.mttr = (
            MttrPredictor()
        )

    def analyze(
        self,
        rootcause_result
    ) -> RiskResult:

        blast_radius = (

            self.blast_radius
            .calculate(
                rootcause_result
            )
        )

        customer_impact = (

            self.customer_impact
            .estimate(
                rootcause_result
            )
        )

        business_impact = (

            self.business_impact
            .estimate(
                rootcause_result
            )
        )

        slo_risk = (

            self.slo_risk
            .calculate(
                rootcause_result
            )
        )

        mttr = (

            self.mttr
            .predict(
                rootcause_result
            )
        )

        impact_assessment = (

            ImpactAssessment(

                customer_impact=(
                    customer_impact
                ),

                business_impact=(
                    business_impact
                ),

                operational_impact=(

                    rootcause_result
                    .root_cause
                    .category
                )
            )
        )

        risk_summary = (

            RiskSummary(

                risk_level=(
                    rootcause_result
                    .severity
                ),

                estimated_mttr_minutes=(
                    mttr
                ),

                slo_risk_percent=(
                    slo_risk
                )
            )
        )

        return RiskResult(

            risk_id=str(
                uuid.uuid4()
            ),

            rootcause_id=(

                rootcause_result
                .rootcause_id
            ),

            service=(

                rootcause_result
                .service
            ),

            priority=(

                rootcause_result
                .priority
            ),

            blast_radius=(
                blast_radius
            ),

            impact_assessment=(
                impact_assessment
            ),

            risk_summary=(
                risk_summary
            ),

            generated_at=(
                datetime.utcnow()
            )
        )