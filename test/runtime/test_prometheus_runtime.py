import asyncio

from ingestion.collectors.prometheus_collector import (
    PrometheusCollector
)


collector = PrometheusCollector()


async def main():

    await collector.collect_cpu_usage()

    print(
        "Prometheus collection completed."
    )


asyncio.run(main())