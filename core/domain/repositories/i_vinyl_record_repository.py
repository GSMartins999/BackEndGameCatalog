from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.vinyl_record import VinylRecord


class IVinylRecordRepository(ABC):
    @abstractmethod
    async def save(self, record: VinylRecord) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, id: str) -> Optional[VinylRecord]:
        pass

    @abstractmethod
    async def find_all(self) -> List[VinylRecord]:
        pass

    @abstractmethod
    async def update(self, record: VinylRecord) -> None:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
