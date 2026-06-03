import logging
import httpx

from ingestion.collectors.base_collector import (
    BaseCollector
)

from ingestion.collectors.parsers.jaeger_parser import (
    parse_jaeger_trace
)

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    TRACES_TOPIC
)


logger = logging.getLogger(
    "sentinel.jaeger.collector"
)


class JaegerCollector(BaseCollector):

    topic = TRACES_TOPIC

    async def collect_traces(

        self,

        service_name: str
    ):

        try:

            async with httpx.AsyncClient(
                timeout=30
            ) as client:

                response = await client.get(

                    f"{settings.JAEGER_URL}/api/traces",

                    params={
                        "service": service_name
                    }
                )

                response.raise_for_status()

                traces = response.json()["data"]

                logger.info(
                    f"Fetched {len(traces)} traces."
                )

                for trace in traces:

                    event = parse_jaeger_trace(
                        trace
                    )

                    if event:

                        await self.publish(
                            event.model_dump()
                        )

        except Exception as e:

            logger.exception(
                f"Jaeger collection failed: {e}"
            )