from .data_lancamento import DataLancamento
from .descricao import Descricao
from .email import Email
from .nome_jogo import NomeDoJogo
from .password import Password
from .url import URL


# Helper functions for creating value objects
def data_lancamento(value):
    from datetime import date
    if isinstance(value, int):
        return DataLancamento(date(value, 1, 1))
    return DataLancamento(value)


def descricao(value: str):
    return Descricao(value)


def nome_jogo(value: str):
    return NomeDoJogo(value)


def url(value: str):
    return URL(value)