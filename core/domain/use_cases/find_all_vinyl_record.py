from typing import List

from ..entities import VinylRecord
from ..repositories import IVinylRecordRepository


class FindAllVinylRecord:
    def __init__(self, vinyl_record_repository: IVinylRecordRepository):
        self.vinyl_record_repository = vinyl_record_repository

    async def execute(self) -> List[VinylRecord]:
        return await self.vinyl_record_repository.find_all()
