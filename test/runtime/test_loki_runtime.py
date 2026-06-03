import asyncio

from ingestion.collectors.loki_collector import (
    LokiCollector
)


collector = LokiCollector()


async def main():

    await collector.collect_logs()

    print(
        "Loki collection completed."
    )


asyncio.run(main())