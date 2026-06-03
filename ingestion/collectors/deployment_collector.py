import logging

from kubernetes import client, config

from ingestion.collectors.base_collector import (
    BaseCollector
)

from ingestion.messaging.topics import (
    DEPLOYMENTS_TOPIC
)


logger = logging.getLogger(
    "sentinel.deployment.collector"
)


class DeploymentCollector(BaseCollector):

    topic = DEPLOYMENTS_TOPIC

    def __init__(self):

        super().__init__()

        self.apps_v1 = None

    def get_client(self):

        if self.apps_v1 is None:

            config.load_kube_config()

            self.apps_v1 = client.AppsV1Api()

        return self.apps_v1

    async def collect_deployments(self):

        try:

            deployments = (
                self.get_client()
                .list_deployment_for_all_namespaces()
            )

            logger.info(
                f"Fetched {len(deployments.items)} deployments."
            )

            for deployment in deployments.items:

                deployment_event = {

                    "deployment_name": (
                        deployment.metadata.name
                    ),

                    "namespace": (
                        deployment.metadata.namespace
                    ),

                    "generation": (
                        deployment.metadata.generation
                    ),

                    "replicas": (
                        deployment.spec.replicas
                    ),

                    "available_replicas": (
                        deployment.status.available_replicas
                    ),

                    "updated_replicas": (
                        deployment.status.updated_replicas
                    ),

                    "unavailable_replicas": (
                        deployment.status.unavailable_replicas
                    ),

                    "strategy": (
                        deployment.spec.strategy.type
                    ),

                    "creation_timestamp": str(
                        deployment.metadata.creation_timestamp
                    ),

                    "labels": (
                        deployment.metadata.labels
                    ),

                    "containers": [

                        {
                            "name": c.name,
                            "image": c.image
                        }

                        for c in deployment.spec.template.spec.containers
                    ]
                }

                await self.publish(
                    deployment_event
                )

        except Exception as e:

            logger.exception(
                f"Deployment collection failed: {e}"
            )