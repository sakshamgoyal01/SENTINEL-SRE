SERVICE_MAP = {

    "payment": "payment-service",

    "payment-api": "payment-service",

    "paymentsvc": "payment-service",

    "checkout": "checkout-service",

    "auth": "auth-service"
}


def normalize_service(service_name: str):

    if not service_name:

        return "unknown-service"

    normalized = SERVICE_MAP.get(
        service_name.lower()
    )

    return normalized or service_name.lower()