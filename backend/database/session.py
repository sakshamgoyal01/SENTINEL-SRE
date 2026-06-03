from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from backend.core.config import (
    get_settings
)

settings = get_settings()

engine = create_async_engine(
    settings.database_url,
    echo=settings.DATABASE_ECHO,
    pool_pre_ping=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_db() -> AsyncGenerator:

    async with SessionLocal() as session:
        yield session