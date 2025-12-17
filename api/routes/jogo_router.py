from typing import List
from fastapi import APIRouter, Depends, HTTPException

from api.dependencies import get_use_case_factory
from api.schemas.jogos_schemas import (
    JogoCreate,
    JogoResponse,
    JogoUpdate,
)
from core.factories.use_case_factory import UseCaseFactory

jogo_router = APIRouter()


@jogo_router.post("/jogos", response_model=JogoResponse)
async def create_jogo(
    jogo: JogoCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    try:
        register_jogo = factory.create_register_jogo()
        created = await register_jogo.execute(
            nome=jogo.nome,
            descricao=jogo.descricao,
            url=jogo.url,
            data_lancamento=jogo.data_lancamento,
        )

        return JogoResponse.from_entity(created)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@jogo_router.get("/jogos", response_model=List[JogoResponse])
async def list_jogos(factory: UseCaseFactory = Depends(get_use_case_factory)):
    list_jogos = factory.create_list_jogos()
    jogos = await list_jogos.execute()
    return [JogoResponse.from_entity(j) for j in jogos]


@jogo_router.put("/jogos/{jogo_id}", response_model=JogoResponse)
async def update_jogo(
    jogo_id: int,
    jogo: JogoUpdate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    try:
        update_jogo = factory.create_update_jogo()
        updated = await update_jogo.execute(
            id_jogo=jogo_id,
            nome=jogo.nome,
            descricao=jogo.descricao,
            url=jogo.url,
            data_lancamento=jogo.data_lancamento,
        )
        return JogoResponse.from_entity(updated)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@jogo_router.delete("/jogos/{jogo_id}", status_code=204)
async def delete_jogo(
    jogo_id: int,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    delete_jogo = factory.create_delete_jogo()
    await delete_jogo.execute(id_jogo=jogo_id)
