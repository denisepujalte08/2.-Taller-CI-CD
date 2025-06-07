from fastapi import FastAPI
from par import es_par_logico

app = FastAPI()


@app.get("/")
def home():
    return {"mensaje": "¡Hola desde FastAPI!"}


@app.get("/es_par")
def es_par(numero: int):
    resultado = "par" if es_par_logico(numero) else "impar"
    return {
        "mensaje": f"El número {numero} es {resultado}."
    }
