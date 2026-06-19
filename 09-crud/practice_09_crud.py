"""
09 - 综合 CRUD 练习

把 Pydantic + 类型提示 + 文件操作 + 异常处理串起来。
"""

import json
from pathlib import Path

from pydantic import BaseModel, Field


# ============================================================
# 第1步：定义 Task 模型
# ============================================================


class Task(BaseModel):
    id: int = Field(ge=1)
    title: str = Field(min_length=1)
    completed: bool = False
    priority: int = Field(default=3, ge=1, le=5)


TaskData = dict[str, object]


# ============================================================
# 第2步：内存数据库
# ============================================================


task_db: dict[int, TaskData] = {}
task_next_id: int = 1


# ============================================================
# 第3步：CRUD 函数
# ============================================================


def list_tasks(completed: bool | None = None) -> list[TaskData]:
    """
    列出任务。
    completed=None -> 全部
    completed=True -> 已完成
    completed=False -> 未完成
    """
    all_tasks = list(task_db.values())
    if completed is None:
        return all_tasks
    return [task for task in all_tasks if task["completed"] == completed]


def create_task(title: str, priority: int = 3) -> TaskData:
    """
    创建任务。
    1. 用 Task 模型校验 title 和 priority
    2. model_dump() 转 dict
    3. 存入 task_db
    4. task_next_id += 1
    5. 返回存入的 dict
    """
    global task_next_id

    task = Task(id=task_next_id, title=title, priority=priority)
    task_data = task.model_dump()
    task_db[task.id] = task_data
    task_next_id += 1
    return task_data


def complete_task(task_id: int) -> TaskData | None:
    """
    标记任务完成。
    如果不存在返回 None。
    否则设置 completed=True，返回更新后的 dict。
    """
    task = task_db.get(task_id)
    if task is None:
        return None
    task["completed"] = True
    return task


def delete_task(task_id: int) -> bool:
    """
    删除任务。存在返回 True，不存在返回 False。
    """
    return task_db.pop(task_id, None) is not None


# ============================================================
# 第4步：文件持久化
# ============================================================


def _resolve_data_path(filename: str | Path) -> Path:
    path = Path(filename)
    if path.is_absolute():
        return path
    return Path(__file__).parent / path


def save_tasks(filename: str | Path = "tasks.json") -> None:
    """
    把 task_db 和 task_next_id 保存到 JSON 文件。
    格式：{"next_id": 5, "tasks": { ... }}
    """
    path = _resolve_data_path(filename)
    payload = {"next_id": task_next_id, "tasks": task_db}

    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def load_tasks(filename: str | Path = "tasks.json") -> None:
    """从文件加载 task_db 和 task_next_id。"""
    global task_db, task_next_id

    path = _resolve_data_path(filename)
    if not path.exists():
        task_db = {}
        task_next_id = 1
        return

    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    raw_tasks = payload.get("tasks", {})
    if not isinstance(raw_tasks, dict):
        raise ValueError("tasks 必须是一个 JSON object")

    loaded_tasks: dict[int, TaskData] = {}
    for raw_task in raw_tasks.values():
        task = Task.model_validate(raw_task)
        loaded_tasks[task.id] = task.model_dump()

    saved_next_id = int(payload.get("next_id", 1))
    next_available_id = max(loaded_tasks, default=0) + 1

    task_db = loaded_tasks
    task_next_id = max(saved_next_id, next_available_id)


# ============================================================
# 第5步：异常处理
# ============================================================


class TaskNotFoundError(Exception):
    """任务不存在时抛出。"""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        self.message = f"任务 {task_id} 不存在"
        super().__init__(self.message)


def safe_delete_task(task_id: int) -> TaskData:
    """
    安全删除：不存在时抛 TaskNotFoundError，不返回 bool。
    """
    task = task_db.pop(task_id, None)
    if task is None:
        raise TaskNotFoundError(task_id)
    return task


# ============================================================
# 验证
# ============================================================


def demo() -> None:
    print("=== Task CRUD 验证 ===")

    task_db.clear()
    global task_next_id
    task_next_id = 1

    t1 = create_task("学习 Pydantic", 1)
    create_task("写日报", 2)
    t3 = create_task("买零食", 4)
    print(f"创建了 {len(list_tasks())} 个任务")

    for task in list_tasks():
        status = "已完成" if task["completed"] else "未完成"
        print(f"  [{task['id']}] {task['title']} (优先级{task['priority']}) {status}")

    complete_task(int(t1["id"]))
    print(f"\n已完成: {len(list_tasks(completed=True))} 个")
    print(f"未完成: {len(list_tasks(completed=False))} 个")

    delete_task(int(t3["id"]))
    print(f"\n删除后剩余: {len(list_tasks())} 个")

    save_tasks()
    print("\n已保存到 tasks.json")

    task_db.clear()
    print(f"清空后: {len(list_tasks())} 个")
    load_tasks()
    print(f"加载后: {len(list_tasks())} 个")

    try:
        safe_delete_task(9999)
        print("错误：应该抛异常但没有")
    except TaskNotFoundError as exc:
        print(f"正确抛出异常: {exc.message}")


if __name__ == "__main__":
    demo()
    print("\n09 综合 CRUD 完成！")
