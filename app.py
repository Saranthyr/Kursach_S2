from flask import Flask
from back.db_conn import conn

conn()

app = Flask(__name__)