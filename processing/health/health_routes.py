from fastapi import APIRouter

from processing.health.processing_health import (
    ProcessingHealth
)

router = APIRouter()


@router.get("/health")

def health():

    return (
        ProcessingHealth.health()
    )