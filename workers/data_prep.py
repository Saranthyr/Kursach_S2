import json
import requests
from workers.location import nearest
from workers.to_geo_json import convert
from back.db_conn import connection


def data_prep(lat, long, table, mode, net):
    closest = nearest(lat,long,table,net,mode)
    if len(closest) != 0:
        routing_key = key_selection('routing')
        get_request = 'https://api.tomtom.com/routing/1/calculateRoute/' + str(lat) + ',' + str(long) + \
                      ':' + str(closest[0]) + ',' + str(closest[1]) + '/json?' \
                      '&traffic=true&travelMode=' + mode + \
                      '&key=' + routing_key
        r = requests.get(get_request)
        t = json.loads(bytes(r.content))
        geodata = convert(t)
        return closest, geodata
    else:
        return 0, 0


def key_selection(key_type):
    conn = connection()
    key = ''
    curs = conn.cursor()
    q = 'select key from keys where key_type = ' + "'" + key_type + "'"
    curs.execute(q)
    for record in curs.fetchall():
        key = record[0]
    curs.close()
    conn.close()
    return key
