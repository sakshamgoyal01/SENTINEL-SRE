SERVICE_DEPENDENCIES = {

    "payment-service": [
        "postgres-db",
        "redis"
    ],

    "checkout-service": [
        "payment-service"
    ]
}


def enrich_topology(event: dict):

    service = event.get("service")

    dependencies = SERVICE_DEPENDENCIES.get(
        service,
        []
    )

    event["dependencies"] = dependencies

    return event