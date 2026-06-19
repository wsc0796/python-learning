from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status

from dependencies import get_todo_service
from models import TodoCreate, TodoRead, TodoUpdate
from service import TodoNotFoundError, TodoService

app = FastAPI(title="Todos API")

TodoServiceDep = Annotated[TodoService, Depends(get_todo_service)]


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Todos API is running"}


@app.post("/todos", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, service: TodoServiceDep) -> TodoRead:
    return service.create_todo(todo)


@app.get("/todos", response_model=list[TodoRead])
def list_todos(service: TodoServiceDep) -> list[TodoRead]:
    return service.list_todos()


@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, service: TodoServiceDep) -> TodoRead:
    try:
        return service.get_todo(todo_id)
    except TodoNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, service: TodoServiceDep) -> None:
    try:
        service.delete_todo(todo_id)
    except TodoNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
