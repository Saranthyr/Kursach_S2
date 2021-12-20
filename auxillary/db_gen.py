import datetime
import json
import timeit
import transliterate
from auxillary.db_tables_gen import tables_generation
from back.db_conn import connection


def generate_data_from_file(filename):
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' started')
    conn = connection()
    cursor = conn.cursor()
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
            q = q + " (id, name, address, phone, seats_count, longitude, latitude) values (%s, %s, %s, %s, %s, %s, %s)" \
                    "on conflict do nothing"
            cursor.execute(q, (int(a[i]['ID']), a[i]['Name'], a[i]['Address'],
                                   a[i]['PublicPhone'][0]['PublicPhone'], a[i]['SeatsCount'],
                                   float(a[i]['Longitude_WGS84']), float(a[i]['Latitude_WGS84'])))
            conn.commit()
        cursor.close()
        conn.close()
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' finished')


def generation():
    try:
        start = timeit.default_timer()
        tables_generation()
        generate_data_from_file("data-4275-2021-11-30-0.json")
        generate_data_from_file("data-4275-2021-11-30-1.json")
        generate_data_from_file("data-4275-2021-11-30-2.json")
        generate_data_from_file("data-4275-2021-11-30-3.json")
        generate_data_from_file("data-4275-2021-11-30-4.json")
        finish = timeit.default_timer()
        print("Time elapsed: " + str(finish - start))
    except Exception as e:
        print(e.__name__)
        pass


generation()
