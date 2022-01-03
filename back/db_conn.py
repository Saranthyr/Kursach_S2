import psycopg2
from config import Config as config


def connection():
    conn = psycopg2.connect(host=config.DB_SETTINGS.db_serv,
                            password=config.DB_SETTINGS.db_pwd,
                            port=config.DB_SETTINGS.db_port,
                            user=config.DB_SETTINGS.db_user,
                            database=config.DB_SETTINGS.db_name
                            )
    return conn
