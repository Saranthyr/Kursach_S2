import asyncio
import timeit

from back.db_conn_async import connection
from exp import get_tables

unique_coords = []
doubles = []

async def coord_check(tablename):
    conn = await connection()
    q = 'select id, longitude, latitude from ' + tablename
    async with conn.transaction():
        async for record in conn.cursor(q):
            if [record[1], record[2]] not in unique_coords:
                unique_coords.append([record[1], record[2]])
            else:
                doubles.append(record[0])

    for d in range(len(doubles)):
        print(str(doubles[d]) + '\n')
    print('done' + str(len(doubles)))



async def run():
    start = timeit.default_timer()
    tasks = []
    for i in await get_tables():
            task = asyncio.create_task(coord_check(i))
            tasks.append(task)
    await asyncio.gather(*tasks)
    finish = timeit.default_timer()
    print("Time elapsed: " + str(finish - start))

asyncio.get_event_loop().run_until_complete(run())


