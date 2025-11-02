import uuid

from ..entities import VinylRecord
from ..repositories import IVinylRecordRepository
from ..value_objects import Name, Photo


class RegisterVinylRecord:
    def __init__(self, vinyl_record_repository: IVinylRecordRepository):
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(
        self,
        band: str,
        album: str,
        year: int,
        number_of_tracks: int,
        photo_url: str,
        user_id: str,
    ) -> VinylRecord:
        record = VinylRecord(
            id=str(uuid.uuid4()),
            band=Name(band),
            album=Name(album),
            year=year,
            number_of_tracks=number_of_tracks,
            photo=Photo(photo_url),
            user_id=user_id,
        )

        await self.vinyl_record_repository.save(record)
        return record
