from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import auth_router, loan_router, user_router, vinyl_router

app = FastAPI(
    title="Empréstimos de Vinis",
    description="API que irá servir os dados para os empréstimos",
    version="0.0.1",
)

origins = [
    "http://http://localhost:3000",  # Vite local
    "https://frontweb20252.vercel.app",  # Produção
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
app.include_router(vinyl_router, prefix="/api", tags=["vinyl"])
app.include_router(loan_router, prefix="/api", tags=["loans"])


@app.get("/")
def read_root():
    return {"msg": "API FastAPI"}
