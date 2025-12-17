from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.domain.entities.jogo import Jogo as JogoEntity
from core.domain.repositories.i_jogo_repository import IJogoRepository
from core.domain.value_objects import (
    NomeDoJogo,
    Descricao,
    URL,
    DataLancamento,
)
from core.infra.orm.jogo import Jogo as JogoModel


class JogoRepository(IJogoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, jogo: JogoEntity) -> None:
        jogo_model = JogoModel(
            id_jogo=jogo.id_jogo,
            nome=jogo.nome.value,
            descricao=jogo.descricao.value,
            url=jogo.url.value,
            data_lancamento=jogo.data_lancamento.value,
        )
        self.session.add(jogo_model)
        await self.session.commit()

    async def find_by_id(self, id_jogo: int) -> Optional[JogoEntity]:
        result = await self.session.execute(
            select(JogoModel).where(JogoModel.id_jogo == id_jogo)
        )
        jogo_model = result.scalar_one_or_none()

        if not jogo_model:
            return None

        return JogoEntity.create(
            id_jogo=jogo_model.id_jogo,
            nome=NomeDoJogo.create(jogo_model.nome),
            descricao=Descricao.create(jogo_model.descricao),
            url=URL.create(jogo_model.url),
            data_lancamento=DataLancamento.create(jogo_model.data_lancamento),
        )

    async def find_all(self) -> List[JogoEntity]:
        result = await self.session.execute(select(JogoModel))
        jogos = result.scalars().all()

        return [
            JogoEntity.create(
                id_jogo=jogo.id_jogo,
                nome=NomeDoJogo.create(jogo.nome),
                descricao=Descricao.create(jogo.descricao),
                url=URL.create(jogo.url),
                data_lancamento=DataLancamento.create(jogo.data_lancamento),
            )
            for jogo in jogos
        ]

    async def update(self, jogo: JogoEntity) -> None:
        result = await self.session.execute(
            select(JogoModel).where(JogoModel.id_jogo == jogo.id_jogo)
        )
        jogo_model = result.scalar_one()

        jogo_model.nome = jogo.nome.value
        jogo_model.descricao = jogo.descricao.value
        jogo_model.url = jogo.url.value
        jogo_model.data_lancamento = jogo.data_lancamento.value

        await self.session.commit()

    async def delete(self, id_jogo: int) -> None:
        result = await self.session.execute(
            select(JogoModel).where(JogoModel.id_jogo == id_jogo)
        )
        jogo_model = result.scalar_one()

        await self.session.delete(jogo_model)
        await self.session.commit()
