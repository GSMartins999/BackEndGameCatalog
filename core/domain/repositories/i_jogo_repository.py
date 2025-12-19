from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.jogo import Jogo


class IJogoRepository(ABC):

    @abstractmethod
    async def save(self, jogo: Jogo) -> None: ...

    @abstractmethod
    async def update(self, jogo: Jogo) -> None: ...

    @abstractmethod
    async def delete(self, id_jogo: int) -> None: ...

    @abstractmethod
    async def find_by_id(self, id_jogo: int) -> Optional[Jogo]: ...

    @abstractmethod
    async def find_all(self) -> List[Jogo]: ...
