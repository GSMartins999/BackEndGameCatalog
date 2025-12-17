from typing import List

from ..entities.jogo import Jogo
from ..repositories.i_jogo_repository import IJogoRepository


class ListJogos:
    def __init__(self, jogo_repository: IJogoRepository):
        self.jogo_repository = jogo_repository

    def execute(self) -> List[Jogo]:
        return self.jogo_repository.find_all()
