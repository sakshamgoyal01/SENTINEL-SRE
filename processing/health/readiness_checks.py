from ingestion.messaging.healthcheck import (
    check_kafka_health
)


class ReadinessChecks:

    @staticmethod
    def kafka_ready():

        return check_kafka_health()

    @staticmethod
    def processing_ready():

        return True