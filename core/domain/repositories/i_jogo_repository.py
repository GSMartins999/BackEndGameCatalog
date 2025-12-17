from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.entities.jogo import Jogo


class IJogoRepository(ABC):

    @abstractmethod
    def save(self, jogo: Jogo) -> None: ...

    @abstractmethod
    def update(self, jogo: Jogo) -> None: ...

    @abstractmethod
    def delete(self, id_jogo: int) -> None: ...

    @abstractmethod
    def find_by_id(self, id_jogo: int) -> Optional[Jogo]: ...

    @abstractmethod
    def find_all(self) -> List[Jogo]: ...
