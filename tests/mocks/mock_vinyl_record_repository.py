from typing import List, Optional

from domain.entities import VinylRecord
from domain.repositories import IVinylRecordRepository


class MockVinylRecordRepository(IVinylRecordRepository):
    def __init__(self):
        self.records: List[VinylRecord] = []

    async def save(self, record: VinylRecord) -> None:
        self.records.append(record)

    async def find_by_id(self, id: str) -> Optional[VinylRecord]:
        return next((record for record in self.records if record.id == id), None)

    async def find_all(self) -> List[VinylRecord]:
        return self.records

    async def update(self, record: VinylRecord) -> None:
        index = next((i for i, r in enumerate(self.records) if r.id == record.id), None)
        if index is not None:
            self.records[index] = record

    async def delete(self, id: str) -> None:
        self.records = [record for record in self.records if record.id != id]
