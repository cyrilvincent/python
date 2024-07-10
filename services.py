import media
import abc
import mock_db
import logging

class AService(abc.ABC):


    def __init__(self):
        self.db = mock_db.books

    @abc.abstractmethod
    def search(self, query) -> list[media.Media]: ...

    @abc.abstractmethod
    def detail(self, id: int) -> media.Media: ...

    @abc.abstractmethod
    def add_to_cart(self, media: media.Media, cart: media.Cart):...

    @abc.abstractmethod
    def validate(self, cart: media.Cart): ...

    @abc.abstractmethod
    def pay(self, cart: media.Cart): ...


class CartService(AService):

    def __init__(self):
        super().__init__()

    def search(self, query: str) -> list[media.Media]:
        return [m for m in self.db if query.strip().upper() in m.title.upper()]

    def detail(self, id: int) -> media.Media:
        return [m for m in self.db if m.id == id][0]

    def add_to_cart(self, media: media.Media, cart: media.Cart):
        cart.medias.append(media)

    def validate(self, cart: media.Cart) -> bool:
        if len(cart.medias) == 0:
            raise ValueError("Can't validate an empy cart")
        return True

    def pay(self, cart: media.Cart):
        logging.warning("Payed")



