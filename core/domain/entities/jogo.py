import dataclasses

from ..value_objects import (
    NomeDoJogo,
    Descricao,
    URL,
    DataLancamento
)


@dataclasses.dataclass
class Jogo:
    id_jogo: int
    nome_do_jogo: NomeDoJogo
    descricao: Descricao
    url: URL
    data_lancamento: DataLancamento
