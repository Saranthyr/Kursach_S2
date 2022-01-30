import asyncio
import timeit
from back.db_conn_async import connection
import math


earth_rad = 6371
coordinates = []

distances = []


def degr_to_rad(degrees):
    return degrees * math.pi/180


async def coordinates_pool(tablename):
    conn = await connection()
    q = 'select id, latitude, longitude from ' + tablename + ' order by id asc'
    async with conn.transaction():
        async for record in conn.cursor(q):
            coordinates.append([record[0], record[1], record[2]])


async def create_coordinates_pool():
    await coordinates_pool('predprijatie_bystrogo_obsluzhivanija_net')


async def check_distance(latitude, longitude):
    start = timeit.default_timer()
    await create_coordinates_pool()
    for coords in coordinates:
        delta_lat = degr_to_rad(latitude - coords[1])
        delta_long = degr_to_rad(longitude - coords[2])
        lat1 = degr_to_rad(coords[1])
        lat2 = degr_to_rad(latitude)
        a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.sin(delta_long/2) * math.sin(delta_long/2)\
            * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distances.append([earth_rad*c, coords[0]])
    finish = timeit.default_timer()
    print("Time elapsed: " + str(finish - start))

    for i in range(len(distances)):
        if distances[i][0] < 5.0:
            print(str(i) + '-' + str(distances[i][1]) + '   ' + str(distances[i][0]))

asyncio.get_event_loop().run_until_complete(check_distance(55.751999, 37.617734))







