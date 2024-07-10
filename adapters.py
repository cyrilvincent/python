import dtos
import media

class MediaAdapter:

    @staticmethod
    def to_detail_dto(m: media.Media) -> dtos.MediaDetailDTO:
        dto = dtos.MediaDetailDTO(
            id=m.id,
            title=m.title,
            price=m.price,
            publisher=None if m.publisher is None else m.publisher.name,
            authors_fullname=[f"{a.first_name} {a.last_name}" for a in m.authors],
        )
        return dto

    @staticmethod
    def to_media_dto(m: media.Media) -> dtos.MediaDetailDTO:
        dto = dtos.MediaDetailDTO(
            id=m.id,
            title=m.title,
            price=m.price,
        )
        return dto

