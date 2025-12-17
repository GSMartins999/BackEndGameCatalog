from core.domain.entities.jogo import Jogo
from core.domain.repositories.i_jogo_repository import IJogoRepository
from core.domain.value_objects import (
    NomeDoJogo,
    Descricao,
    URL,
    DataLancamento
)
import random


class RegisterJogo:
    def __init__(self, jogo_repository: IJogoRepository):
        self.jogo_repository = jogo_repository

    def execute(self, *, nome: str, descricao: str, url: str, data_lancamento):
        jogo = Jogo.create(
            id_jogo=random.randint(1, 100000),
            nome=NomeDoJogo.create(nome),
            descricao=Descricao.create(descricao),
            url=URL.create(url),
            data_lancamento=DataLancamento.create(data_lancamento),
        )

        self.jogo_repository.save(jogo)
        return jogo
