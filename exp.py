import asyncio
from back.db_conn_async import connection


async def exp():
    conn = await connection()
    async with conn.transaction():
        async for record in conn.cursor("select table_name from information_schema.tables where table_schema = 'public'"):
            print(record)

asyncio.get_event_loop().run_until_complete(exp())