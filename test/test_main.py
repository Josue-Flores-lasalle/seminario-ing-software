from fastapi.testclient import  TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API"}



def test_create_task():
    task = { "id": 1, "title": "Participar Seminario", "description": "prueba", "completed": False}
    response = client.post("/tasks", json=task)
    assert response.status_code == 200
    assert response.json() == task

def test_get_task():
    task_id = 1
    task = {"id": 1, "title": "Participar Seminario", "description": "prueba", "completed": False}
    client.post("/tasks", json=task)
    response = client.get(f"/task/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id