# test_db.py

import asyncio

from sqlalchemy import text

from backend.database.session import (
    AsyncSessionLocal
)


async def test():

    async with (
        AsyncSessionLocal()
    ) as db:

        result = await db.execute(

            text(
                "SELECT 1"
            )
        )

        print(
            result.scalar()
        )


asyncio.run(
    test()
)