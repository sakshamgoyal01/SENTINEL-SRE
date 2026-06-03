import logging

from prometheus_api_client import (
    PrometheusConnect
)

from ingestion.collectors.base_collector import (
    BaseCollector
)

from ingestion.collectors.parsers.prometheus_parser import (
    parse_prometheus_metric
)

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    METRICS_TOPIC
)


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(
    "sentinel.prometheus.collector"
)


class PrometheusCollector(BaseCollector):

    topic = METRICS_TOPIC

    def __init__(self):

        self.prom = PrometheusConnect(

            url=settings.PROMETHEUS_URL,

            disable_ssl=True
        )

    async def collect_metric(

        self,

        query: str
    ):

        try:

            metric_data = self.prom.custom_query(
                query=query
            )

            logger.info(
                f"Fetched {len(metric_data)} metrics."
            )

            for raw_metric in metric_data:

                event = parse_prometheus_metric(
                    raw_metric
                )

                await self.publish(
                    event.model_dump()
                )

        except Exception as e:

            logger.exception(
                f"Prometheus collection failed: {e}"
            )

    async def collect_cpu_usage(self):

        query = """
        100 - (
          avg(
            rate(
              node_cpu_seconds_total{mode="idle"}[1m]
            )
          ) * 100
        )
        """

        await self.collect_metric(query)