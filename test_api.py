from fastapi.testclient import TestClient
from par_api import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Hola desde FastAPI!"}


def test_es_par_par():
    response = client.get("/es_par?numero=2")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "El número 2 es par."


def test_es_par_impar():
    response = client.get("/es_par?numero=3")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "El número 3 es impar."
