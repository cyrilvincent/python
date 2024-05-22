from typing import List, Sequence, Type

import db_context
import entities
import abc
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
import media


class AService(metaclass=abc.ABCMeta):

    def __init__(self, session: Session):
        self.session = session


class ManageCartService(AService):

    def __init__(self, session: Session):
        super().__init__(session)

    def search(self, query: str) -> Sequence[entities.Media]:
        return session.execute(select(entities.Media).where(entities.Media.title.ilike(f"%{query}%"))).scalars().all()

    def get_detail(self, id: int) -> entities.Media:
        return session.get(entities.Media, id)

    def add_to_cart(self, media: media.Media):
        cart = session.get(entities.Cart, 1) # bidouille
        if cart is None:
            cart = entities.Cart()
            session.add(cart)
        if media not in cart.medias:
            cart.medias.append(media)
            session.commit()

    def validate(self) -> bool:
        cart = session.get(entities.Cart, 1)
        if len(cart.medias) > 0:
            cart.is_validate = True
            session.commit()

    def get_total_net_price(self) -> float:
        cart = session.execute(select(entities.Cart, 1).options(joinedload(entities.Cart.medias))).scalars().first()
        return sum([m.price for m in cart.medias])


if __name__ == '__main__':
    context = db_context.FormationContext()
    context.create_engine()
    session = context.get_session()
    service = ManageCartService(session)
    res = service.search("y")
    media = service.get_detail(res[0].id)
    service.add_to_cart(media)
    print(service.get_total_net_price())





