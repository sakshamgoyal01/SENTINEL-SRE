import asyncio

from ingestion.collectors.jaeger_collector import (
    JaegerCollector
)


collector = JaegerCollector()


async def main():

    await collector.collect_traces(
        "payment-service"
    )

    print(
        "Jaeger collection completed."
    )


asyncio.run(main())