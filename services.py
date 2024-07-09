import media
import abc
import mock_db

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

    pass



