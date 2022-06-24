from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
