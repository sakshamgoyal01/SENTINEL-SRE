import logging

from backend.persistence.topic_registry import (
    TOPIC_HANDLERS
)

logger = logging.getLogger(__name__)


class EventPersistenceManager:

    def __init__(
        self,
        handlers: dict | None = None,
    ):
        self.handlers = handlers or {}

    async def persist_event(
        self,
        topic: str,
        payload: dict,
    ) -> None:

        handler = self.handlers.get(
            topic
        )

        if handler is None:

            logger.error(
                "No persistence handler "
                "registered for topic %s",
                topic
            )

            raise ValueError(
                f"No handler registered "
                f"for topic {topic}"
            )

        await handler.persist(
            payload
        )

    @classmethod
    def from_registry(
        cls,
        handler_instances: dict,
    ):

        handlers = {}

        for (
            topic,
            handler_class
        ) in TOPIC_HANDLERS.items():

            instance = (
                handler_instances.get(
                    handler_class
                )
            )

            if instance is None:

                raise ValueError(
                    f"Missing handler instance "
                    f"for {handler_class}"
                )

            handlers[topic] = instance

        return cls(
            handlers=handlers
        )