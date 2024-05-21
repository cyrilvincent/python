import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Float, CHAR, create_engine, Column, ForeignKey, Boolean, UniqueConstraint, \
    Table, Index, Date
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.engine import Engine
from typing import Optional, List
import config

class Base:
    __allow_unmapped__ = True

Base = declarative_base(cls=Base)

# Base = declarative_base()


class FormationContext:

    def __init__(self, connection_string=config.connection_string):
        self.engine: Optional[Engine] = None
        self.connection_string = connection_string

    def create_engine(self, echo=False, create_all=True):
        self.engine = create_engine(self.connection_string, echo=echo)
        if create_all:
            Base.metadata.create_all(self.engine)

    def get_session(self, expire_on_commit=False):
        Session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=expire_on_commit)
        return Session()


if __name__ == '__main__':
    print(sqlalchemy.__version__)
    context = FormationContext()
    context.create(echo=True)
