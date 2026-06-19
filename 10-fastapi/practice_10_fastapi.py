"""
10 - FastAPI 练习

运行前：
    pip install fastapi uvicorn

运行：
    uvicorn practice_10_fastapi:app --reload

然后打开：
    http://127.0.0.1:8000/docs
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


# ============================================================
# 步骤1：创建 FastAPI 实例
# ============================================================


app = FastAPI(title="Python Learning API")


# ============================================================
# 步骤2：定义 Item 模型
# ============================================================


class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)


# ============================================================
# 步骤3：根路由
# ============================================================


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI 已启动"}


# ============================================================
# 步骤4：路径参数
# ============================================================


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}


# ============================================================
# 步骤5：查询参数
# ============================================================


@app.get("/items")
def list_items(
    q: Annotated[str, Query(min_length=1)] = "all",
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
) -> dict[str, int | str]:
    return {"q": q, "skip": skip, "limit": limit}


# ============================================================
# 步骤6：POST 用 Pydantic 校验
# ============================================================


@app.post("/items")
def create_item(item: Item) -> dict[str, Item]:
    return {"received": item}


# ============================================================
# 步骤7：完整的 Task CRUD（衔接 09 综合 CRUD）
# ============================================================


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(default=3, ge=1, le=5)


class TaskRead(TaskCreate):
    id: int = Field(ge=1)
    completed: bool = False


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[int, TaskRead] = {}
        self._next_id = 1

    def list_tasks(self, completed: bool | None = None) -> list[TaskRead]:
        tasks = list(self._tasks.values())
        if completed is None:
            return tasks
        return [task for task in tasks if task.completed == completed]

    def create_task(self, task: TaskCreate) -> TaskRead:
        created = TaskRead(
            id=self._next_id,
            title=task.title,
            priority=task.priority,
            completed=False,
        )
        self._tasks[created.id] = created
        self._next_id += 1
        return created

    def get_task(self, task_id: int) -> TaskRead:
        task = self._tasks.get(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="任务不存在")
        return task

    def complete_task(self, task_id: int) -> TaskRead:
        task = self.get_task(task_id)
        completed = task.model_copy(update={"completed": True})
        self._tasks[task_id] = completed
        return completed

    def delete_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise HTTPException(status_code=404, detail="任务不存在")
        del self._tasks[task_id]


task_service = TaskService()


def get_task_service() -> TaskService:
    return task_service


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, service: TaskServiceDep) -> TaskRead:
    return service.create_task(task)


@app.get("/tasks", response_model=list[TaskRead])
def list_tasks(
    service: TaskServiceDep,
    completed: Annotated[bool | None, Query()] = None,
) -> list[TaskRead]:
    return service.list_tasks(completed=completed)


@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, service: TaskServiceDep) -> TaskRead:
    return service.get_task(task_id)


@app.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def complete_task(task_id: int, service: TaskServiceDep) -> TaskRead:
    return service.complete_task(task_id)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskServiceDep) -> None:
    service.delete_task(task_id)


if __name__ == "__main__":
    print(
        """
运行方式：
uvicorn practice_10_fastapi:app --reload
然后打开 http://127.0.0.1:8000/docs
"""
    )
