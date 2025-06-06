from fastapi import FastAPI
from par import es_par_logico

app = FastAPI()


@app.get("/")
def home():
    return {"mensaje": "¡Hola desde FastAPI!"}


@app.get("/es_par")
def es_par(numero: int):
    return {
        "numero": numero,
        "es_par": es_par_logico(numero)
    }
