import psycopg2
from back.config import Config as config

def connection():
    conn = psycopg2.connect(host=config.DB_SETTINGS.db_serv,
                            port=config.DB_SETTINGS.db_port,
                            user=config.DB_SETTINGS.db_user,
                            password=config.DB_SETTINGS.db_pwd,
                            database=config.DB_SETTINGS.db_name
                            )
    return conn