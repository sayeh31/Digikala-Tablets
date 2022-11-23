
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config.cfg as cfg


SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{cfg.mysql["user"]}:{cfg.mysql["passwd"]}@{cfg.mysql["host"]}/{cfg.mysql["db"]}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()