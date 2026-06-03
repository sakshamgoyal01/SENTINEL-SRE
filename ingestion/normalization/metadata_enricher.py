def enrich_metadata(

    event: dict,

    cluster: str = "sentinel-local",

    environment: str = "development",

    team: str = "backend-engineering",

    region: str = "local",

    namespace: str = "default"
):

    event["cluster"] = cluster

    event["environment"] = environment

    event["team"] = team

    event["region"] = region

    event["namespace"] = namespace

    return event