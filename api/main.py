from fastapi import FastAPI
from api.routes.user_router import router as user_router

app = FastAPI(
    title="Empréstimos de Vinis",
    description="API que irá servir os dados para os empréstimos",
    version="0.0.1",
)

app.include_router(user_router, prefix="/api", tags=["users"])


@app.get("/")
def read_root():
    return {"msg": "API FastAPI"}
