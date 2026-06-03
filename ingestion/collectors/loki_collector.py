import logging
import httpx

from ingestion.collectors.base_collector import (
    BaseCollector
)

from ingestion.collectors.parsers.loki_parser import (
    parse_loki_log
)

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    LOGS_TOPIC
)


logger = logging.getLogger(
    "sentinel.loki.collector"
)


class LokiCollector(BaseCollector):

    topic = LOGS_TOPIC

    async def collect_logs(self):

        try:

            query = '{job="varlogs"}'

            async with httpx.AsyncClient(
                timeout=30
            ) as client:

                response = await client.get(

                    f"{settings.LOKI_URL}/loki/api/v1/query_range",

                    params={
                        "query": query,
                        "limit": 100
                    }
                )

                response.raise_for_status()

                data = response.json()

                streams = data["data"]["result"]

                logger.info(
                    f"Fetched {len(streams)} log streams."
                )

                for stream_data in streams:

                    stream = stream_data["stream"]

                    values = stream_data["values"]

                    for value in values:

                        event = parse_loki_log(
                            stream,
                            value
                        )

                        await self.publish(
                            event.model_dump()
                        )

        except Exception as e:

            logger.exception(
                f"Loki collection failed: {e}"
            )