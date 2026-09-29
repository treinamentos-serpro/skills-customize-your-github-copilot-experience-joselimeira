"""Starter code para persistir tarefas em SQLite com FastAPI."""

from collections.abc import Generator

from fastapi import Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy import Boolean, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(120))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskResponse(TaskCreate):
    id: int


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Persistent Tasks API")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    # TODO: Consultar e retornar todas as tarefas.
    pass


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    # TODO: Buscar a tarefa ou lançar HTTPException(status_code=404).
    pass


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # TODO: Criar, salvar, confirmar e retornar uma tarefa.
    pass


@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    # TODO: Atualizar a tarefa, confirmar a alteração e retorná-la.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # TODO: Remover a tarefa e retornar Response(status_code=204).
    pass


# Execute com:
# uvicorn starter-code:app --reload
