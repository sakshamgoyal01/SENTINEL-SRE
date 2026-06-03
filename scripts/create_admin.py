import asyncio

from backend.database.session import SessionLocal

from backend.models.auth.user import User

from backend.auth.password import (
    hash_password,
)


async def main():
    async with SessionLocal() as session:
        admin = User(
            email="admin@sentinel.com",
            username="admin",
            password_hash=hash_password(
                "Admin@123"
            ),
            is_active=True,
            is_superuser=True,
        )

        session.add(admin)

        await session.commit()

        print(
            "Admin user created"
        )


if __name__ == "__main__":
    asyncio.run(main())