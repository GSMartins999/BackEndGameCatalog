from sqlalchemy import Column, Integer, String, Date
from .base import Base


class Jogo(Base):
    __tablename__ = "jogos"

    id_jogo = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(500), nullable=False)
    url = Column(String, nullable=False)
    data_lancamento = Column(Date, nullable=False)
