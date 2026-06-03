NAMESPACE_ENV_MAP = {

    "prod": "production",

    "staging": "staging",

    "dev": "development"
}


def map_namespace_environment(
    namespace: str
):

    return NAMESPACE_ENV_MAP.get(
        namespace,
        "development"
    )