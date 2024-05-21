import enum
from typing import List
import sqlalchemy

import config
import db_context as context
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy import Integer, String, Float, CHAR, create_engine, Column, ForeignKey, Boolean, UniqueConstraint, \
    Table, Index, Date, select, Enum


class Publisher(context.Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, )
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.id} {self.name}"


if __name__ == '__main__':
    ctx = context.FormationContext(config.connection_string)
    ctx.create_engine(echo=True)
    session = ctx.get_session()
    p1 = Publisher()
    p1.name = "Cyril"
    session.add(p1)
    p1 = Publisher()
    p1.name = "Vincent"
    session.add(p1)
    session.commit()
    publisher = session.get(Publisher, 3)
    print(publisher)
    publishers = session.execute(select(Publisher)).scalars().all()
    print(type(publishers))
    for p in publishers:
        print(type(p))
        print(p)
    #session.delete(publisher)
    publisher.name += "X"
    session.commit()
