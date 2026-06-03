from kafka import KafkaAdminClient

from ingestion.config.ingestion_settings import settings


def check_kafka_health():

    try:

        admin = KafkaAdminClient(

            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
        )

        topics = admin.list_topics()

        return {

            "status": "healthy",

            "topics": list(topics)
        }

    except Exception as e:

        return {

            "status": "unhealthy",

            "error": str(e)
        }