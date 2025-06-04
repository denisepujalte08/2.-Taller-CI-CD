from fastapi import FastAPI


app = FastAPI()


def es_par_logico(numero: int) -> bool:
    return numero % 2 != 0


@app.get("/")
def home():
    return {"mensaje": "¡Hola desde FastAPI!"}


@app.get("/es_par")
def es_par(numero: int):
    return {
        "numero": numero,
        "es_par": es_par_logico(numero)
    }
