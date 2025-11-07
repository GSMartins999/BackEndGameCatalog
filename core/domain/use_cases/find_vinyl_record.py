from typing import Optional

from ..entities import VinylRecord
from ..repositories import IVinylRecordRepository


class FindVinylRecord:
    def __init__(self, vinyl_record_repository: IVinylRecordRepository):
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(self, id: str) -> Optional[VinylRecord]:
        return await self.vinyl_record_repository.find_by_id(id)
