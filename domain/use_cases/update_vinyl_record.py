from typing import Optional

from ..entities import VinylRecord
from ..repositories import IVinylRecordRepository
from ..value_objects import Name, Photo


class UpdateVinylRecord:
    def __init__(self, vinyl_record_repository: IVinylRecordRepository):
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(
        self,
        id: str,
        band: Optional[str] = None,
        album: Optional[str] = None,
        year: Optional[int] = None,
        number_of_tracks: Optional[int] = None,
        photo_url: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> VinylRecord:
        record = await self.vinyl_record_repository.find_by_id(id)

        if not record:
            raise ValueError("Vinyl record not found")

        updated_record = VinylRecord(
            id=record.id,
            band=Name(band) if band else record.band,
            album=Name(album) if album else record.album,
            year=year if year is not None else record.year,
            number_of_tracks=number_of_tracks
            if number_of_tracks is not None
            else record.number_of_tracks,
            photo=Photo(photo_url) if photo_url else record.photo,
            user_id=user_id if user_id else record.user_id,
        )

        await self.vinyl_record_repository.update(updated_record)
        return updated_record
