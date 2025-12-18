from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importando as instâncias exatas de cada arquivo
from api.routes.auth_router import auth_router
from api.routes.user_router import user_router
from api.routes.jogo_router import jogo_router

app = FastAPI(
    title="Jogos GameCatalog",
    description="API que irá servir os dados para os empréstimos",
    version="0.0.1",
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://gamecatalog-chi.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro das rotas usando os objetos importados
app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(jogo_router, prefix="/api", tags=["jogos"])

@app.get("/")
def read_root():
    return {"msg": "API FastAPI rodando com sucesso!"}