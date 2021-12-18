import datetime
import json
import asyncio
import transliterate
from auxillary.db_tables_gen import miracle_worker
from back.db_conn_async import connection


async def insert_data_from_file(filename):
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' started')
    conn = await connection()
    with open(filename, "r", encoding='utf-8') as f:
        a = json.load(f)
        for i in range(len(a)):
            type_obj = str(transliterate.translit(a[i]['TypeObject'], reversed=True))
            type_obj = type_obj.replace(' ', '_')
            type_obj = type_obj.replace('(', '')
            type_obj = type_obj.replace(')', '')
            net_obj = transliterate.translit(a[i]['IsNetObject'], reversed=True)
            tablename = type_obj + '_' + net_obj
            q = "insert into "
            q = q + tablename
            q = q + " (id, name, address, phone, seats_count, longitude, latitude) values ($1, $2, $3, $4, $5, $6, $7)"
            await conn.execute(q, int(a[i]['ID']), a[i]['Name'], a[i]['Address'],
                                   a[i]['PublicPhone'][0]['PublicPhone'], a[i]['SeatsCount'],
                                   float(a[i]['Longitude_WGS84']), float(a[i]['Latitude_WGS84']))
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' finished')


async def data_gen():
    try:
        await asyncio.gather(
            insert_data_from_file("data-4275-2021-11-30-0.json"),
            insert_data_from_file("data-4275-2021-11-30-1.json"),
            insert_data_from_file("data-4275-2021-11-30-2.json"),
            insert_data_from_file("data-4275-2021-11-30-3.json"),
            insert_data_from_file("data-4275-2021-11-30-4.json")
        )
    except Exception as e:
        print(e.__name__)
        pass

miracle_worker()
asyncio.get_event_loop().run_until_complete(data_gen())
