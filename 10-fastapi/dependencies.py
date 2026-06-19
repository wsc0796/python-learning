"""
FastAPI 依赖注入配置。

这里创建真实对象，接口函数通过 Depends(get_task_service) 使用它。
"""

from pathlib import Path

from repository import JsonTaskRepository
from service import TaskService


DATA_FILE = Path(__file__).with_name("tasks.json")

task_repository = JsonTaskRepository(DATA_FILE)
task_service = TaskService(task_repository)


def get_task_service() -> TaskService:
    return task_service
