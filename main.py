from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title:str
    description:str
    completed:bool = False


# Base de Datos simulada
tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    if any(existing_task.id == task.id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for item in tasks:
        if item.id == task_id:
            return tasks
    raise HTTPException(status_code=404, detail="Tarea no encontrada")