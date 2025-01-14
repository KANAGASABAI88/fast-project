from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:8895@localhost/alchemy'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# connect_args={"check_same_thread":False}

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlash=False)

Base = declarative_base()
