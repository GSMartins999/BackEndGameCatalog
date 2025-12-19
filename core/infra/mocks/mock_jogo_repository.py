from typing import List, Optional
from core.domain.entities.jogo import Jogo

class MockJogoRepository:
    def __init__(self):
        self.jogos: List[Jogo] = []

    async def save(self, jogo: Jogo) -> Jogo:
        self.jogos.append(jogo)
        return jogo

    async def find_by_id(self, id_jogo: int) -> Optional[Jogo]:
        for jogo in self.jogos:
            if jogo.id_jogo == id_jogo:
                return jogo
        return None

    async def delete(self, id_jogo: int):
        jogo = await self.find_by_id(id_jogo)
        if not jogo:
            raise ValueError("Jogo not found")
        self.jogos.remove(jogo)

    async def update(self, jogo: Jogo) -> Jogo:
        for index, j in enumerate(self.jogos):
            if j.id_jogo == jogo.id_jogo:
                self.jogos[index] = jogo
                return jogo
        raise ValueError("Jogo not found")

    async def find_all(self) -> List[Jogo]:
        return self.jogos

    async def list_all(self) -> List[Jogo]:
        return self.jogos
