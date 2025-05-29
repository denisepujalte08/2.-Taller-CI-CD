from fastapi import FastAPI

app = FastAPI()


@app.get("/es_par")
def es_par(numero: int):
    return {
        "numero": numero,
        "es_par": numero % 2 == 0
    }
