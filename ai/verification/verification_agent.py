import uuid

from datetime import datetime

from ai.models.verification_check import (
    VerificationCheck
)

from ai.models.verification_result import (
    VerificationResult
)

from ai.verification.health_checker import (
    HealthChecker
)

from ai.verification.metric_verifier import (
    MetricVerifier
)

from ai.verification.log_verifier import (
    LogVerifier
)

from ai.verification.trace_verifier import (
    TraceVerifier
)


class VerificationAgent:

    def __init__(self):

        self.health_checker = (
            HealthChecker()
        )

        self.metric_verifier = (
            MetricVerifier()
        )

        self.log_verifier = (
            LogVerifier()
        )

        self.trace_verifier = (
            TraceVerifier()
        )

    def verify(
        self,
        execution_result
    ) -> VerificationResult:

        health_ok = (
            self.health_checker
            .check(
                execution_result
            )
        )

        metrics_ok = (
            self.metric_verifier
            .verify(
                execution_result
            )
        )

        logs_ok = (
            self.log_verifier
            .verify(
                execution_result
            )
        )

        traces_ok = (
            self.trace_verifier
            .verify(
                execution_result
            )
        )

        checks = [

            VerificationCheck(

                check_type="health",

                passed=health_ok,

                details="Health check passed"
            ),

            VerificationCheck(

                check_type="metrics",

                passed=metrics_ok,

                details="Metric verification passed"
            ),

            VerificationCheck(

                check_type="logs",

                passed=logs_ok,

                details="Log verification passed"
            ),

            VerificationCheck(

                check_type="traces",

                passed=traces_ok,

                details="Trace verification passed"
            )
        ]

        verified = all(

            [
                health_ok,
                metrics_ok,
                logs_ok,
                traces_ok
            ]
        )

        return VerificationResult(

            verification_id=str(
                uuid.uuid4()
            ),

            execution_id=(
                execution_result
                .execution_id
            ),

            service=(
                execution_result
                .service
            ),

            verified=verified,

            health_status=(
                "HEALTHY"
                if verified
                else "UNHEALTHY"
            ),

            verification_result=(
                "SUCCESS"
                if verified
                else "FAILED"
            ),

            checks=checks,

            generated_at=(
                datetime.utcnow()
            )
        )