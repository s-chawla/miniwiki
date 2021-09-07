from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_database():
    """
    This functions creates the database
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    This function returns the instance of the database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
