import logging
import sys

import structlog


def configure_logging():

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="iso"
            ),
            structlog.processors.JSONRenderer()
        ]
    )

    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(message)s"
    )