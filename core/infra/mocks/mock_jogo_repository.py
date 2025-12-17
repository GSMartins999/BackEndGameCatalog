from core.domain.repositories.i_jogo_repository import IJogoRepository
from core.domain.entities.jogo import Jogo
from typing import List, Optional


class MockJogoRepository(IJogoRepository):

    def __init__(self):
        self._jogos: List[Jogo] = []

    def save(self, jogo: Jogo) -> None:
        self._jogos.append(jogo)

    def find_by_id(self, id_jogo: int) -> Optional[Jogo]:
        return next((j for j in self._jogos if j.id_jogo == id_jogo), None)

    def find_all(self) -> List[Jogo]:
        return self._jogos

    def update(self, jogo: Jogo) -> None:
        for index, jogo_atual in enumerate(self._jogos):
            if jogo_atual.id_jogo == jogo.id_jogo:
                self._jogos[index] = jogo
                return

    def delete(self, id_jogo: int) -> None:
        self._jogos = [
            jogo for jogo in self._jogos
            if jogo.id_jogo != id_jogo
        ]
