import json
import requests
import flask
from config import Config as config
from test2 import nearest
from to_geo_json import convert

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    long = float(flask.request.form.get('longitude', 37.475096))
    lat = float(flask.request.form.get('latitude', 55.728985))
    closest = nearest(lat, long)
    get_request = 'https://api.tomtom.com/routing/1/calculateRoute/' + str(lat) + ',' + str(long) +\
                  ':' + str(closest[0]) + ',' + str(closest[1]) + '/json?' \
                  '&traffic=true&key=' + config.API_ACCESS.api_key
    r = requests.get(get_request)
    t = json.loads(bytes(r.content))
    geodata = convert(t)
    return flask.\
        render_template('test.html',
                        longitude=long,
                        latitude=lat,
                        closest_lat=closest[0],
                        closest_long=closest[1],
                        api_key=config.API_ACCESS.api_key,
                        route=geodata)



