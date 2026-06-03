import logging

from kubernetes import client, config

from ingestion.collectors.base_collector import (
    BaseCollector
)

from ingestion.collectors.parsers.k8s_parser import (
    parse_k8s_event
)

from ingestion.messaging.topics import (
    K8S_EVENTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.k8s.collector"
)


class KubernetesEventsCollector(BaseCollector):

    topic = K8S_EVENTS_TOPIC

    def __init__(self):

        self.v1 = None

    def get_client(self):

        if self.v1 is None:

            config.load_kube_config()

            self.v1 = client.CoreV1Api()

        return self.v1

    async def collect_events(self):

        try:

            events = (
                self.get_client()
                .list_event_for_all_namespaces()
            )

            logger.info(
                f"Fetched {len(events.items)} K8s events."
            )

            for event in events.items:

                parsed_event = parse_k8s_event(
                    event
                )

                await self.publish(
                    parsed_event
                )

        except Exception as e:

            logger.exception(
                f"K8s event collection failed: {e}"
            )