from backend.api.crud_router import CRUDRouter
from backend.api.dependencies.knowledge import get_knowledge_service
from backend.schemas.intelligence.knowledge import (
    KnowledgeResponse,
    CreateKnowledgeRequest,
    UpdateKnowledgeRequest,
)

router = CRUDRouter(
    service_dependency=get_knowledge_service,
    response_schema=KnowledgeResponse,
    create_schema=CreateKnowledgeRequest,
    update_schema=UpdateKnowledgeRequest,
    prefix="",
    tags=["Knowledge"],
).router