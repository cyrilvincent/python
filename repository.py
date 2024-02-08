from typing import List
import media


class GenericRepository:

    def __init__(self,path:str):
        pass

    def load(self) -> List[media.Book]:
        pass

    def save(self, books: List[media.Book]):
        pass

class BookCsvRepository(GenericRepository):

