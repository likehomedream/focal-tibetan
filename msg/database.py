from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
