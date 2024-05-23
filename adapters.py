import entities
import dtos

class Adapter:

    @staticmethod
    def from_media_to_media_detail_dto(from_: entities.Media) -> dtos.MediaDetailDTO:
        dto = dtos.MediaDetailDTO(
            id=from_.id,
            title=from_.title,
            price=from_.price,
            type=str(from_.type),
            publisher_name=from_.publisher.name if from_.publisher else "",
            author_fullname=f"{from_.authors[0].first_name} {from_.authors[0].last_name}" if len(from_.authors) > 0 else ""
        )
        return dto


