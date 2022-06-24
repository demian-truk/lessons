"""
Создать функции для подключения и создания базы данных.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists

DB_USER = "osenstarosti"
DB_PASSWORD = "neurosmetanka808"
DB_NAME = "my_database"
DB_ECHO = True


def setup_db_engine() -> Engine:
    return create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True)


def create_database_if_not_exists(engine: Engine) -> bool:
    if not database_exists(engine.url):
        create_database(engine.url)
        return True
    return False
