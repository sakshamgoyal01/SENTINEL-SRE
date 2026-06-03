from ingestion.messaging.producer import producer

from ingestion.messaging.consumer import consumer


class KafkaManager:

    @staticmethod
    def close():

        producer.close()

        consumer.close()
