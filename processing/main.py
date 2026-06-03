from fastapi import FastAPI

from prometheus_client import (
    make_asgi_app
)

from processing.health.health_routes import (
    router
)

app = FastAPI()

app.include_router(router)

metrics_app = make_asgi_app()

app.mount(
    "/metrics",
    metrics_app
)