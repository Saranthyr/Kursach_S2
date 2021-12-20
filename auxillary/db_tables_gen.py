import datetime
import json
import transliterate
from back.db_conn import connection


def generate_table_from_file(filename):
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' started')
    conn = connection()
    cursor = conn.cursor()
    with open(filename, "r", encoding='utf-8') as f:
        a = json.load(f)
        for i in range(len(a)):
            q = "create table if not exists "
            type_obj = str(transliterate.translit(a[i]['TypeObject'], reversed=True))
            type_obj = type_obj.replace(' ', '_')
            type_obj = type_obj.replace('(', '')
            type_obj = type_obj.replace(')', '')
            net_obj = transliterate.translit(a[i]['IsNetObject'], reversed=True)
            tablename = type_obj + '_' + net_obj
            q = q + tablename
            q = q + ' (id integer PRIMARY KEY, ' \
                    'name text, ' \
                    'address text, ' \
                    'phone text, ' \
                    'seats_count integer, ' \
                    'longitude float,' \
                    'latitude float)'
            cursor.execute(q)
            conn.commit()
    cursor.close()
    conn.close()
    print(str(datetime.datetime.now().time()) + ' ' + filename + ' finished')


def tables_generation():
    generate_table_from_file("data-4275-2021-11-30-0.json")
    generate_table_from_file("data-4275-2021-11-30-1.json")
    generate_table_from_file("data-4275-2021-11-30-2.json")
    generate_table_from_file("data-4275-2021-11-30-3.json")
    generate_table_from_file("data-4275-2021-11-30-4.json")

    return 0
