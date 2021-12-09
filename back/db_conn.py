import psycopg2
from back.config import Config as config

def conn():
    con = psycopg2.connect(
        host=config.DB_SETTINGS.db_serv,
        port=config.DB_SETTINGS.db_port,
        user=config.DB_SETTINGS.db_user,
        password=config.DB_SETTINGS.db_pwd,
        dbname=config.DB_SETTINGS.db_name
    )
    return con