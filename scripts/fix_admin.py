import asyncio

from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models.auth.user import User

from backend.auth.password import (
    hash_password,
)


async def main():
    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.username == "admin"
            )
        )

        user = result.scalar_one()

        user.email = (
            "admin@sentinel.com"
        )

        user.password_hash = (
            hash_password(
                "Admin@123"
            )
        )

        await session.commit()

        print(
            "Admin updated"
        )


asyncio.run(main())