from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Float, CHAR, Column, ForeignKey, Boolean, UniqueConstraint, \
    Table, Index, Date
from sqlalchemy.orm import relationship, Session
from sqlalchemy.engine import Engine
from typing import Optional, List
import config
import sqlalchemy
import asyncio


class Base:
    __allow_unmapped__ = True


Base = declarative_base(cls=Base)

# Base = declarative_base()


class FormationContext:

    def __init__(self, connection_string=config.connection_string):
        self.engine: Optional[AsyncEngine] = None
        self.connection_string = connection_string

    def create_engine(self, echo=False, create_all=True):
        self.engine = create_async_engine(self.connection_string, echo=echo)
        if create_all:
            Base.metadata.create_all(self.engine)

    def get_session_async(self, expire_on_commit=False) -> async_sessionmaker[AsyncSession]:
        session_async = async_sessionmaker(bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=expire_on_commit)
        return session_async

