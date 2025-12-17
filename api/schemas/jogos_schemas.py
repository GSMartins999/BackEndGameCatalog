from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


class JogoCreate(BaseModel):
    nome: str
    descricao: str
    url: str
    data_lancamento: date


class JogoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    url: Optional[str] = None
    data_lancamento: Optional[date] = None


class JogoResponse(BaseModel):
    id_jogo: int
    nome: str
    descricao: str
    url: str
    data_lancamento: date

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="before")
    @classmethod
    def map_domain_to_schema(cls, v):
        """
        Converte a entidade de domínio Jogo para um schema de resposta.
        """
        # Se já for dict (testes / serialização)
        if isinstance(v, dict):
            return v

        return {
            "id_jogo": v.id_jogo,
            "nome": v.nome.value,
            "descricao": v.descricao.value,
            "url": v.url.value,
            "data_lancamento": v.data_lancamento.value,
        }

    @classmethod
    def from_entity(cls, jogo):
        return cls(
            id_jogo=jogo.id_jogo,
            nome=jogo.nome.value,
            descricao=jogo.descricao.value,
            url=jogo.url.value,
            data_lancamento=jogo.data_lancamento.value,
        )
