from processing.health.readiness_checks import (
    ReadinessChecks
)


class ProcessingHealth:

    @staticmethod
    def health():

        return {

            "status": "UP",

            "messaging": (
                ReadinessChecks
                .kafka_ready()
            ),

            "processing": (
                ReadinessChecks
                .processing_ready()
            )
        }