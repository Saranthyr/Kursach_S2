import flask
from data_prep import data_prep


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == "POST":
        long = float(flask.request.form.get('longitude'))
        lat = float(flask.request.form.get('latitude'))
        table_selection = str(flask.request.form.get("table"))
        mode = str(flask.request.form.get("mode"))
        net = bool(flask.request.form.get("net"))
        closest, geodata = data_prep(lat, long, table_selection, mode, net)
        if closest == 0 and geodata == 0:
            return flask.make_response(flask.jsonify({"message": "No results been found"}), 230)
        else:
            return flask.make_response(flask.jsonify({'geodata': geodata,
                                                      'closest_longitude': closest[1],
                                                      'closest_latitude': closest[0],
                                                      'longitude': long,
                                                      'latitude': lat,
                                                      'place_name': closest[2],
                                                      'address': closest[3],
                                                      'phone': closest[4],
                                                      'seats': closest[5]}), 200)
    else:
        return flask.\
            render_template('tomtomservicever.html')



