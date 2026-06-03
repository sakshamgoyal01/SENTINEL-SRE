import logging

from processing.aggregation.metric_aggregator import (
    MetricAggregator
)

from processing.aggregation.log_aggregator import (
    LogAggregator
)

from processing.aggregation.trace_aggregator import (
    TraceAggregator
)

from processing.aggregation.deployment_aggregator import (
    DeploymentAggregator
)

from processing.aggregation.k8s_aggregator import (
    KubernetesAggregator
)

logger = logging.getLogger(
    "sentinel.aggregation.manager"
)


class AggregationManager:

    def __init__(self):

        self.metric_aggregator = (
            MetricAggregator()
        )

        self.log_aggregator = (
            LogAggregator()
        )

        self.trace_aggregator = (
            TraceAggregator()
        )

        self.deployment_aggregator = (
            DeploymentAggregator()
        )

        self.k8s_aggregator = (
            KubernetesAggregator()
        )

    def aggregate(
        self,
        event
    ):

        if event.event_type == "metric":

            return (
                self.metric_aggregator
                .aggregate(event)
            )

        if event.event_type == "log":

            return (
                self.log_aggregator
                .aggregate(event)
            )

        if event.event_type == "trace":

            return (
                self.trace_aggregator
                .aggregate(event)
            )

        if event.event_type == "deployment":

            return (
                self.deployment_aggregator
                .aggregate(event)
            )

        if event.event_type == "k8s_event":

            return (
                self.k8s_aggregator
                .aggregate(event)
            )

        return None