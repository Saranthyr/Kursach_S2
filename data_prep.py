import json
import requests
from test2 import nearest
from to_geo_json import convert
from config import Config as config


def data_prep(lat, long):
    closest = nearest(lat, long)
    get_request = 'https://api.tomtom.com/routing/1/calculateRoute/' + str(lat) + ',' + str(long) + \
                  ':' + str(closest[0]) + ',' + str(closest[1]) + '/json?' \
                                                                  '&traffic=true&key=' + config.API_ACCESS.api_key
    r = requests.get(get_request)
    t = json.loads(bytes(r.content))
    geodata = convert(t)
    return closest, geodata