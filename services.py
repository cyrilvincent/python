from typing import List

import db_context
import entities
import abc

import media


class AService(metaclass=abc.ABCMeta):

    def __init__(self, context: db_context.FormationContext):
        self.context = context


class ManageCartService(AService):

    def __init__(self, context: db_context.FormationContext):
        super().__init__(context)


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





