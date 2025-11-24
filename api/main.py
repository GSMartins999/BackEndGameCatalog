from fastapi import FastAPI

app = FastAPI(
    title="Empréstimos de Vinis",
    description="API que irá servir os dados para os empréstimos",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"msg": "API FastAPI"}
