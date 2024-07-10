from pydantic import BaseModel


class MediaDetailDTO(BaseModel):
    id: int
    title: str
    price: float
    publisher_name: str | None = None
    authors_fullname: list[str] = []


class MediaDTO(BaseModel):
    id: int
    title: str
    price: float


class CartDTO(BaseModel):
    id: int
    medias: list[MediaDTO] = []
