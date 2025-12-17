from datetime import date
from typing import Optional

from ..entities.jogo import Jogo
from ..repositories.i_jogo_repository import IJogoRepository
from ..value_objects import NomeDoJogo, Descricao, URL, DataLancamento


class EditJogo:
    def __init__(self, jogo_repository: IJogoRepository):
        self.jogo_repository = jogo_repository

    def execute(
        self,
        *,
        id_jogo: int,
        nome_do_jogo: Optional[str] = None,
        descricao: Optional[str] = None,
        url: Optional[str] = None,
        data_lancamento: Optional[date] = None,
    ) -> Jogo:

        jogo = self.jogo_repository.find_by_id(id_jogo)
        if not jogo:
            raise ValueError("Jogo não encontrado para edição.")

        nome_vo = NomeDoJogo(nome_do_jogo) if nome_do_jogo else jogo.nome_do_jogo
        descricao_vo = Descricao(descricao) if descricao else jogo.descricao
        url_vo = URL(url) if url else jogo.url
        data_vo = (
            DataLancamento(data_lancamento)
            if data_lancamento
            else jogo.data_lancamento
        )

        jogo_atualizado = Jogo(
            id_jogo=jogo.id_jogo,
            nome_do_jogo=nome_vo,
            descricao=descricao_vo,
            url=url_vo,
            data_lancamento=data_vo,
        )

        self.jogo_repository.update(jogo_atualizado)

        return jogo_atualizado
