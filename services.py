from typing import List

import db_context
import entities
import abc
from sqlalchemy.orm import Session

import media


class AService(metaclass=abc.ABCMeta):

    def __init__(self, session: Session):
        self.session = session


class ManageCartService(AService):

    def __init__(self, session: Session):
        super().__init__(session)


    def search(self, query: str) -> List[entities.Media]:
        pass

    def get_detail(self, id: int) -> entities.Media:
        pass

    def add_to_cart(self, media: media.Media):
        pass

    def validate(self) -> bool:
        pass
        # verif si panier non vide

    def get_total_net_price(self) -> float:
        pass

if __name__ == '__main__':
    context = db_context.FormationContext()
    session = context.get_session()
    service = ManageCartService(seesion)



