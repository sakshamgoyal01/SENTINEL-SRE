import json
import logging

from kafka import KafkaConsumer
from kafka.errors import KafkaError

from ingestion.config.ingestion_settings import settings


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(
    "sentinel.messaging.consumer"
)


def get_consumer(
    topic: str,
    group_id: str
):

    consumer = KafkaConsumer(

        topic,

        bootstrap_servers=(
            settings.KAFKA_BOOTSTRAP_SERVERS
        ),

        auto_offset_reset="latest",

        enable_auto_commit=True,

        group_id=group_id,

        value_deserializer=lambda m:
        json.loads(
            m.decode("utf-8")
        ),

        consumer_timeout_ms=30000
    )

    logger.info(
        f"Consumer subscribed to {topic}"
    )

    return consumer


def process_message(message):

    logger.info(
        f"Processing event: {message}"
    )


def consume(
    topic: str,
    group_id: str
):

    logger.info(
        f"Kafka consumer started for {topic}"
    )

    try:

        consumer = get_consumer(
            topic,
            group_id
        )

        for message in consumer:

            logger.info(
                f"Received message: {message.value}"
            )

            process_message(
                message.value
            )

    except KafkaError as e:

        logger.error(
            f"Kafka consumer error: {e}"
        )

    except Exception as e:

        logger.exception(
            f"Unexpected consumer error: {e}"
        )