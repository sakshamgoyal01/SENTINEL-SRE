import json
import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError

from ingestion.config.ingestion_settings import settings


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(
    "sentinel.messaging.producer"
)


producer = None


def get_producer():

    global producer

    if producer is None:

        producer = KafkaProducer(

            bootstrap_servers=
            settings.KAFKA_BOOTSTRAP_SERVERS,

            value_serializer=lambda v:
            json.dumps(
                v,
                default=str
            ).encode("utf-8"),

            compression_type="gzip",

            acks="all",

            retries=5,

            linger_ms=10,

            batch_size=16384,

            max_block_ms=10000
        )

    return producer


def delivery_report(record_metadata):

    logger.info(

        f"Message delivered to "
        f"{record_metadata.topic} "
        f"partition={record_metadata.partition}"
    )


def send_event(
    topic: str,
    event: dict
):

    try:

        producer = get_producer()

        future = producer.send(
            topic,
            event
        )

        record_metadata = future.get(
            timeout=10
        )

        delivery_report(
            record_metadata
        )

    except KafkaError as e:

        logger.error(
            f"Kafka send failed: {e}"
        )

    except Exception as e:

        logger.exception(
            f"Unexpected producer error: {e}"
        )

        if topic == "sentinel.dlq":

            return

        try:

            producer = get_producer()

            dlq_event = {

                "original_topic": topic,

                "error": str(e),

                "payload": str(event)
            }

            future = producer.send(
                "sentinel.dlq",
                dlq_event
            )

            future.get(timeout=10)

            logger.warning(
                "Event routed to DLQ."
            )

        except Exception as dlq_error:

            logger.exception(
                f"DLQ routing failed: {dlq_error}"
            )