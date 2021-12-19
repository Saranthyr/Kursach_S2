
from back.db_conn_async import connection
import json
import flask


app = flask.Flask(__name__)


@app.route('/main')
def test():
    return flask.render_template('test.html')



