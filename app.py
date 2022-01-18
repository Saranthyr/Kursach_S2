import flask
from data_prep import data_prep, key_selection


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == "POST":
        long = float(flask.request.form.get('longitude'))
        lat = float(flask.request.form.get('latitude'))
        closest, geodata = data_prep(lat, long)
        return flask.jsonify({'geodata': geodata,
                              'closest_longitude': closest[1],
                              'closest_latitude': closest[0],
                              'longitude': long,
                              'latitude': lat})
    else:
        return flask.\
            render_template('tomtomservicever.html')



