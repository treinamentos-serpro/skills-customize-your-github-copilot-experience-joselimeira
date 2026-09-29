"""Starter code para a assignment Building REST APIs com FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


tasks = [
    {"id": 1, "title": "Aprender FastAPI", "completed": False},
    {"id": 2, "title": "Criar uma API REST", "completed": False},
]


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


@app.get("/tasks")
def list_tasks():
    # TODO: Retornar todas as tarefas.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Encontrar a tarefa pelo ID ou retornar um erro 404.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: Criar uma tarefa, adicionar um ID e salvá-la na lista.
    pass


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # TODO: Atualizar uma tarefa existente ou retornar um erro 404.
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: Remover uma tarefa existente ou retornar um erro 404.
    pass


# Execute com:
# uvicorn starter-code:app --reload
