import asyncio
import logging

from ingestion.collectors.scheduler.collection_scheduler import (
    run_collectors
)

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "sentinel.ingestion"
)


async def main():

    logger.info(
        "Starting ingestion layer..."
    )

    await run_collectors()


if __name__ == "__main__":

    asyncio.run(
        main()
    )