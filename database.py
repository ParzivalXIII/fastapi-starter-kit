# PostgreSQL Database Setup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
import models

DB_HOST = "localhost"
DB_NAME = "yourdbname"
DB_USER = "youruser"
DB_PASSWORD = "yourpassword"
DB_PORT = 5432

URL_DATABASE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    """Initialize the database by creating all tables."""
    models.Base.metadata.create_all(bind=engine)

def get_db():
    """
    Get a database session.
    Yields:
        Session: A SQLAlchemy database session
    Usage:
        with get_db() as db:
            # use db session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
