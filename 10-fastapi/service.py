"""
业务层。

这里做 CRUD，但不关心 HTTP，也不关心数据具体存在什么地方。
"""

from models import TaskCreate, TaskRead
from repository import TaskRepository


class TaskNotFoundError(Exception):
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"任务 {task_id} 不存在")


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        
        self.repository = repository

    def list_tasks(self, completed: bool | None = None) -> list[TaskRead]:
        tasks = self.repository.list_tasks()
        if completed is None:
            return tasks
        return [task for task in tasks if task.completed == completed]

    def create_task(self, task_create: TaskCreate) -> TaskRead:
        tasks = self.repository.list_tasks()
        next_id = max((task.id for task in tasks), default=0) + 1
        task = TaskRead(
            id=next_id,
            title=task_create.title,
            priority=task_create.priority,
            completed=False,
        )
        tasks.append(task)
        self.repository.save_tasks(tasks)
        return task

    def get_task(self, task_id: int) -> TaskRead:
        for task in self.repository.list_tasks():
            if task.id == task_id:
                return task
        raise TaskNotFoundError(task_id)

    def complete_task(self, task_id: int) -> TaskRead:
        tasks = self.repository.list_tasks()

        for index, task in enumerate(tasks):
            if task.id == task_id:
                completed_task = task.model_copy(update={"completed": True})
                tasks[index] = completed_task
                self.repository.save_tasks(tasks)
                return completed_task

        raise TaskNotFoundError(task_id)

    def delete_task(self, task_id: int) -> None:
        tasks = self.repository.list_tasks()
        remaining_tasks = [task for task in tasks if task.id != task_id]

        if len(remaining_tasks) == len(tasks):
            raise TaskNotFoundError(task_id)

        self.repository.save_tasks(remaining_tasks)
