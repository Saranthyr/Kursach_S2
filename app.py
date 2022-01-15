from back.db_conn import connection
import json
import flask

from test2 import nearest

app = flask.Flask(__name__)


@app.route('/')
def test():
    long = flask.request.form.get('longitude', 37.617734)
    lat = flask.request.form.get('latitude', 55.751999)
    closest = nearest(lat, long)
    return flask.\
        render_template('test.html', longitude=long, latitude=lat, closest_lat=closest[0], closest_long=closest[1])



