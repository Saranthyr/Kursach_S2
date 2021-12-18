from dotenv import load_dotenv
import os

class Database_Settings():
    load_dotenv('../.flaskenv')
    _environ = os.environ

    db_serv: str = _environ.get("DB_HOST", None)
    db_port: int = _environ.get("DB_PORT", None)
    db_name: str = _environ.get("DB_NAME", None)
    db_user: str = _environ.get("DB_USER", None)
    db_pwd: str = _environ.get("DB_PASSWORD", None)

class Config():
    DB_SETTINGS = Database_Settings()
