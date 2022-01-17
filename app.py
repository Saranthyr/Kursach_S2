import flask
from config import Config as config
from data_prep import data_prep


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def test(lat = 55.728985, long = 37.475096):
    if flask.request.method=="POST":
        long = float(flask.request.form.get('longitude'))
        lat = float(flask.request.form.get('latitude'))
        closest, geodata = data_prep(lat, long)
        return flask.jsonify({'geodata': geodata,
                              'closest_longitude': closest[1],
                              'closest_latitude': closest[0],
                              'longitude': long,
                              'latitude': lat})
    else:
        closest, geodata = data_prep(lat, long)
        return flask.\
            render_template('tomtomservicever.html',
                            longitude=long,
                            latitude=lat,
                            closest_lat=closest[0],
                            closest_long=closest[1],
                            api_key=config.API_ACCESS.api_key,
                            route=geodata)



