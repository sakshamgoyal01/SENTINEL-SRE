from datetime import datetime


collector_health_registry = {}


def update_collector_health(

    collector_name: str,

    status: str,

    events_processed: int = 0,

    error: str | None = None
):

    collector_health_registry[
        collector_name
    ] = {

        "status": status,

        "last_run": (
            datetime.utcnow().isoformat()
        ),

        "events_processed": events_processed,

        "error": error
    }


def get_collector_health():

    return collector_health_registry