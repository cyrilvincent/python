import enum
from typing import List
import sqlalchemy
import config
import db_context as context
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy import Integer, String, Float, CHAR, SMALLINT, create_engine, Column, ForeignKey, Boolean, UniqueConstraint, CheckConstraint, \
    Table, Index, Date, select, Enum


class Publisher(context.Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, )
    name = Column(String, nullable=False, index=True)
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
    medias = relationship("Media", secondary=media_author, back_populates="authors")

    __table_args__ = (UniqueConstraint('first_name', 'last_name'),)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

cart_media = Table('cart_media', context.Base.metadata,
                     Column('media_id', ForeignKey('media.id'), primary_key=True),
                     Column('cart_id', ForeignKey('cart.id'), primary_key=True)
                     )


class Media(context.Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, )
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    type = Column(Enum(MediaEnum), nullable=False)
    nb_page = Column(Integer)
    awards = Column(Integer, nullable=False, default=0)
    publisher_id = Column(ForeignKey('publisher.id'))
    publisher: Publisher = relationship(Publisher, back_populates="medias") # many_to_zero
    authors: List[Author] = relationship(Author, secondary=media_author, back_populates="medias")
    carts = relationship("Cart", secondary=cart_media, back_populates="medias")
    def __repr__(self):
        return f"{self.id} {self.title} {self.price}"


class Cart(context.Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, )
    medias: List[Media] = relationship("Media", secondary=cart_media, back_populates="carts")
    is_validate = Column(Boolean, default=False)


if __name__ == '__main__':
    ctx = context.FormationContext(config.connection_string)
    ctx.create_engine(echo=True)
    session = ctx.get_session()
    # p1 = Publisher()
    # p1.name = "Cyril"
    # session.add(p1)
    # p1 = Publisher()
    # p1.name = "Vincent"
    # session.add(p1)
    # session.commit()
    # publisher = session.get(Publisher, 1)
    # print(publisher)
    # publishers = (session.execute(
    #     select(Publisher)
    #     .where(Publisher.name == "Vincent"))
    #               .scalars().all())
    # print(type(publishers))
    # for p in publishers:
    #     print(type(p))
    #     print(p)
    # #session.delete(publisher)
    # publisher.name += "X"
    # session.commit()
    m = Media()
    m.title = "Python"
    m.price = 10
    m.type = MediaEnum.book
    session.add(m)
    #p1 = session.get(Publisher, 1)
    p1 = Publisher()
    p1.name = "Nouveau"
    m.publisher = p1
    session.commit()
    m = session.get(Media, 3)
    print(m.publisher.name)
    res = session.execute(
        select(Media)
        .options(joinedload(Media.publisher))
    ).scalars().first()
    res = session.execute(select(Media).join(Publisher).where(Publisher.name.ilike_("vincent%"))).scalars().first()
    # print(res.publisher) # Pas bon car lazy (2 requêtes)
    res = session.execute(select(Media).options(joinedload(Media.publisher)).join(Publisher).where(Publisher.name == "Vincent")).scalars().first()
    # print(res.publisher)  # ok
    res = session.execute(select(Publisher).options(joinedload(Publisher.medias)).where(Publisher.id == 2)).scalars().first()


