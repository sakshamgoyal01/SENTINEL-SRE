import asyncio

from ingestion.collectors.prometheus_collector import (
    PrometheusCollector
)


collector = PrometheusCollector()

asyncio.run(
    collector.collect_cpu_usage()
)