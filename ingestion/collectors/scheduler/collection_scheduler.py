import asyncio
import logging

from ingestion.collectors.prometheus_collector import (
    PrometheusCollector
)

from ingestion.collectors.loki_collector import (
    LokiCollector
)

from ingestion.collectors.jaeger_collector import (
    JaegerCollector
)

from ingestion.collectors.k8s_events_collector import (
    KubernetesEventsCollector
)

from ingestion.collectors.deployment_collector import (
    DeploymentCollector
)


logger = logging.getLogger(
    "sentinel.scheduler"
)


prometheus_collector = (
    PrometheusCollector()
)

loki_collector = LokiCollector()

jaeger_collector = JaegerCollector()

k8s_collector = (
    KubernetesEventsCollector()
)

deployment_collector = (
    DeploymentCollector()
)


async def run_collectors():

    while True:

        logger.info(
            "Starting telemetry collection cycle."
        )

        await asyncio.gather(

            prometheus_collector.collect_cpu_usage(),

            loki_collector.collect_logs(),

            jaeger_collector.collect_traces(
                service_name="payment-service"
            ),

            k8s_collector.collect_events(),

            deployment_collector.collect_deployments()
        )

        logger.info(
            "Telemetry collection cycle completed."
        )

        await asyncio.sleep(30)