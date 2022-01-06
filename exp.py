import asyncio
from back.db_conn_async import connection


async def get_tables():
    conn = await connection()
    tables = []
    async with conn.transaction():
        async for record in conn.cursor("select table_name from information_schema.tables where table_schema = 'public'"):
            tables.append(record[0])
    return tables


async def get_names_list(tablename):
    conn = await connection()
    q = 'select name from ' + tablename
    file = tablename + '.txt'
    t = []
    async with conn.transaction():
            async for record in conn.cursor(q):
                if record[0] not in t:
                    t.append(record[0])
    with open(file, mode='a+') as f:
        for i in t:
            f.write(i)
            f.write('\n')
        f.close()


async def run():
    for i in await get_tables():
        await get_names_list(i)



asyncio.get_event_loop().run_until_complete(run())