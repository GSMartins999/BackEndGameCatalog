from ..repositories.i_jogo_repository import IJogoRepository


class RemoveJogo:
    def __init__(self, jogo_repository: IJogoRepository):
        self.jogo_repository = jogo_repository

    async def execute(self, id_jogo: int) -> None:
        jogo = await self.jogo_repository.find_by_id(id_jogo)

        if not jogo:
            raise ValueError("Jogo not found")

        await self.jogo_repository.delete(id_jogo)
