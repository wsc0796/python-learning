"""
FastAPI 入口。

这一层负责 HTTP：路由、状态码、参数接收、错误响应。
业务逻辑在 service.py，这一层只做"翻译"——把 HTTP 请求翻译成 service 调用。
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, status

from dependencies import get_task_service
from models import TaskCreate, TaskRead
from service import TaskNotFoundError, TaskService

# 需求①：创建 FastAPI 应用实例（整个服务的入口）
app = FastAPI(title="Task CRUD API")

# 需求②：定义依赖注入类型（FastAPI 用 Depends 自动获取 service）
# Annotated[类型, 取货方式] = 把类型标签和获取方式打包成一个变量
TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


# 需求③：根路由，确认服务已启动
@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Task CRUD API 已启动"}


# 需求④：创建任务
# - 请求体用 TaskCreate 校验（只需要 title、priority）
# - 响应体用 TaskRead 规范输出（多了 id 和 completed）
# - 201 状态码表示"资源已创建"
@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, service: TaskServiceDep) -> TaskRead:
    return service.create_task(task)


# 需求⑤：查看全部任务，支持按完成状态筛选
# - 不传 completed → 返回全部
# - 传 completed=true → 只返回已完成的
# - 传 completed=false → 只返回未完成的
@app.get("/tasks", response_model=list[TaskRead])
def list_tasks(
    service: TaskServiceDep,
    completed: Annotated[bool | None, Query()] = None,
) -> list[TaskRead]:
    return service.list_tasks(completed=completed)


# 需求⑥：查看单条任务
# - {task_id} 是路径参数，FastAPI 自动解析并转为 int
# - 找不到时，把业务异常 TaskNotFoundError 翻译成 HTTP 404
@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, service: TaskServiceDep) -> TaskRead:
    try:
        return service.get_task(task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# 需求⑦：标记任务为已完成
# - PATCH 方法：只修改部分字段（completed: false → true）
# - 使用 model_copy(update={"completed": True}) 不改原对象
@app.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def complete_task(task_id: int, service: TaskServiceDep) -> TaskRead:
    try:
        return service.complete_task(task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# 需求⑧：删除任务
# - 204 状态码表示"已删除，无返回内容"
# - 返回类型是 None（没有响应体）
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskServiceDep) -> None:
    try:
        service.delete_task(task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
