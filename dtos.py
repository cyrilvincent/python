from typing import List

from pydantic import BaseModel

class MediaDetailDTO(BaseModel):

    id: int
    title: str
    price: float
    type: str
    publisher_name: str
    author_fullname: str


class MediaDTO(BaseModel):
    id: int
    title: str
    price: float


class CartDTO(BaseModel):
    id: int
    medias: List[MediaDTO] = []



