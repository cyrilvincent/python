import enum
from typing import List

import sqlalchemy
import db_context as context
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy import Integer, String, Float, CHAR, create_engine, Column, ForeignKey, Boolean, UniqueConstraint, \
    Table, Index, Date, select, Enum


class Publisher(context.Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, )
    name = Column(String, nullable=False)
    medias = relationship("Media", back_populates="publisher")

    def __repr__(self):
        return f"{self.id} {self.name}"


class MediaEnum(enum.Enum):
    book = 1
    cd = 2
    dvd = 3


media_author = Table('media_author', context.Base.metadata,
                     Column('media_id', ForeignKey('media.id'), primary_key=True),
                     Column('author_id', ForeignKey('author.id'), primary_key=True)
                     )


class Author(context.Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, )
    first_name = Column(String)
    last_name = Column(String, nullable=False)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    __table_args__ = (UniqueConstraint('first_name', 'last_name'),)

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name}"


class Media(context.Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, )
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    type = Column(Enum(MediaEnum), nullable=False)
    nb_page = Column(Integer)
    publisher_id = Column(ForeignKey('publisher.id'))
    publisher: Publisher = relationship(Publisher, back_populates="medias")
    authors: List[Author] = relationship(Author, secondary=media_author)

    def __repr__(self):
        return f"{self.id} {self.title} {self.price}"


if __name__ == '__main__':
    print(sqlalchemy.__version__)
    context = context.FormationContext()
    context.create(echo=True)
    # p = Publisher()
    # p.name = "Vincent"
    # context.session.add(p)
    # context.session.commit()
    # res = context.session.get(Publisher, 1)
    # print(res)
    # res.name += "X"
    # context.session.commit()
    # res = context.session.execute(select(Publisher)).scalars().all()
    # print(res)
    # res = context.session.execute(select(Publisher).where(Publisher.name == "Vincent")).scalars().first()
    # print(res)
    # m = Media()
    # m.title = "Python"
    # m.type = BookEnum.book
    # m.price = 10.0
    # m.publisher = p
    # context.session.add(m)
    # context.session.commit()
    # res = context.session.execute(select(Media).options(joinedload(Media.publisher))).scalars().first()
    # print(res.publisher)
    # res = context.session.execute(select(Media).join(Publisher).where(Publisher.name == "Vincent")).scalars().first()
    # print(res.publisher) # Pas bon car lazy (2 requêtes)
    # res = context.session.execute(select(Media).options(joinedload(Media.publisher)).join(Publisher).where(Publisher.name == "Vincent")).scalars().first()
    # print(res.publisher)  # ok
    # res = context.session.execute(select(Publisher).options(joinedload(Publisher.medias)).where(Publisher.id == 2)).scalars().first()
    # print(res.medias)
    a = Author("Cyril", "Vincent")
    m = context.session.get(Media, 1)
    m.authors.append(a)
    context.session.commit()
    # Puis voir unique et index
    # Migration = alembic





