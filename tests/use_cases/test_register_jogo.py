from datetime import date
from core.domain.entities.jogo import Jogo
from core.domain.value_objects import NomeDoJogo, Descricao, URL, DataLancamento

class RegisterJogo:
    def __init__(self, jogo_repository):
        self.jogo_repository = jogo_repository
        self._id_counter = 1  # contador para gerar IDs

    async def execute(self, *, nome: str, descricao: str, url: str, data_lancamento: date):
        jogo = Jogo(
            id_jogo=self._id_counter,
            nome_do_jogo=NomeDoJogo(nome),
            descricao=Descricao(descricao),
            url=URL(url),
            data_lancamento=DataLancamento(data_lancamento)
        )
        self._id_counter += 1
        await self.jogo_repository.save(jogo)
        return jogo
