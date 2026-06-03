# scripts/list_users.py

import asyncio

from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models.auth.user import User


async def main():
    async with SessionLocal() as session:
        result = await session.execute(
            select(User)
        )

        users = result.scalars().all()

        for user in users:
            print(
                user.email,
                user.username
            )


asyncio.run(main())