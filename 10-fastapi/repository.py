"""
数据访问层。

这一层负责“数据存在哪里”和“怎么读写”。
业务层不直接操作 JSON 文件，而是依赖 TaskRepository 这个行为约定。
"""

import json
from pathlib import Path
from typing import Protocol

from models import TaskRead


class TaskRepository(Protocol):
    def list_tasks(self) -> list[TaskRead]:
        ...

    def save_tasks(self, tasks: list[TaskRead]) -> None:
        ...


class JsonTaskRepository:
    def __init__(self, filename: str | Path) -> None:
        self.filename = Path(filename)

    def list_tasks(self) -> list[TaskRead]:
        if not self.filename.exists():
            return []

        with self.filename.open("r", encoding="utf-8") as file:
            payload = json.load(file)

        raw_tasks = payload.get("tasks", [])
        if not isinstance(raw_tasks, list):
            raise ValueError("tasks.json 里的 tasks 必须是列表")

        return [TaskRead.model_validate(raw_task) for raw_task in raw_tasks]

    def save_tasks(self, tasks: list[TaskRead]) -> None:
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        payload = {"tasks": [task.model_dump() for task in tasks]}

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
