import asyncio

from backend.database.session import SessionLocal

from backend.models.auth.role import Role


async def main():
    async with SessionLocal() as session:

        roles = [
            Role(
                name="ADMIN",
                description="Platform Administrator",
            ),
            Role(
                name="SRE",
                description="Site Reliability Engineer",
            ),
            Role(
                name="VIEWER",
                description="Read Only User",
            ),
        ]

        session.add_all(roles)

        await session.commit()

        print("Roles created")


asyncio.run(main())