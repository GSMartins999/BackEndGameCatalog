from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth_router, user_router, jogo_router

app = FastAPI(
    title="Jogos GameCatalog",
    description="API que irá servir os dados para os empréstimos",
    version="0.0.1",
)

origins = [
    "http://localhost:3000",  # Next local
    "http://127.0.0.1:3000",  # Next local
    "https://gamecatalog-chi.vercel.app/",  # Produção
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # lista de origens confiáveis
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique ["GET", "POST"]
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(jogo_router, prefix="/api", tags=["jogos"])


@app.get("/")
def read_root():
    return {"msg": "API FastAPI"}