"""
09 — 综合 CRUD 练习
把 Pydantic + 类型提示 + 文件操作串起来。
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import json
from pydantic import BaseModel, Field
from typing import Optional


# ============================================================
# 第1步：定义 Task 模型
# ============================================================
# TODO: 补全 Task 模型
# id: int
# title: str (至少1字符)
# completed: bool (默认 False)
# priority: int (1-5, 默认 3)

class Task(BaseModel):
    # 你的代码...
    pass


# ============================================================
# 第2步：内存数据库
# ============================================================
# task_db = {任务id: 任务dict}
# task_next_id = 下一个可用id

task_db: dict[int, dict] = {}
task_next_id: int = 1


# ============================================================
# 第3步：CRUD 函数
# ============================================================

def list_tasks(completed: Optional[bool] = None) -> list[dict]:
    """
    列出任务。
    completed=None → 全部
    completed=True → 已完成
    completed=False → 未完成
    """
    all_tasks = list(task_db.values())
    if completed is None:
        return all_tasks
    # TODO: 用列表推导式筛选
    return [t for t in all_tasks if t["completed"] == completed]


def create_task(title: str, priority: int = 3) -> dict:
    """
    创建任务。
    1. 用 Task 模型校验 title 和 priority
    2. model_dump() 转 dict
    3. 存入 task_db
    4. task_next_id += 1
    5. 返回存入的 dict
    """
    global task_next_id
    # 你的代码...
    # task = Task(id=task_next_id, title=title, priority=priority)
    pass


def complete_task(task_id: int) -> Optional[dict]:
    """
    标记任务完成。
    如果不存在返回 None。
    否则设置 completed=True，返回更新后的 dict。
    """
    # 你的代码...
    pass


def delete_task(task_id: int) -> bool:
    """
    删除任务。存在返回 True，不存在返回 False。
    提示：dict.pop(key, default) 如果 key 不存在返回 default
    """
    # 你的代码...
    pass


# ============================================================
# 第4步：文件持久化
# ============================================================

def save_tasks(filename: str = "tasks.json"):
    """
    把 task_db 和 task_next_id 保存到 JSON 文件。
    格式：{"next_id": 5, "tasks": { ... }}
    """
    # 你的代码...
    # json.dump({"next_id": task_next_id, "tasks": task_db}, f, ensure_ascii=False, indent=2)
    pass


def load_tasks(filename: str = "tasks.json"):
    """从文件加载 task_db 和 task_next_id"""
    global task_db, task_next_id
    # 你的代码...
    pass


# ============================================================
# 第5步：异常处理
# ============================================================

class TaskNotFoundError(Exception):
    """任务不存在时抛出"""
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.message = f"任务 {task_id} 不存在"
        super().__init__(self.message)


def safe_delete_task(task_id: int) -> dict:
    """
    安全删除：不存在时抛 TaskNotFoundError，不返回 bool。
    """
    # 你的代码...
    pass


# ============================================================
# 验证
# ============================================================

if __name__ == "__main__":
    print("=== Task CRUD 验证 ===")

    # 创建
    t1 = create_task("学习 Pydantic", 1)
    t2 = create_task("写日报", 2)
    t3 = create_task("买零食", 4)
    print(f"创建了 {len(list_tasks())} 个任务")

    # 查看全部
    for t in list_tasks():
        print(f"  [{t['id']}] {t['title']} (优先级{t['priority']}) {'✅' if t['completed'] else '⬜'}")

    # 标记完成
    complete_task(t1["id"])
    print(f"\n已完成: {len(list_tasks(completed=True))} 个")
    print(f"未完成: {len(list_tasks(completed=False))} 个")

    # 删除
    delete_task(t3["id"])
    print(f"\n删除后剩余: {len(list_tasks())} 个")

    # 持久化
    save_tasks()
    print("\n已保存到 tasks.json")

    # 清空内存再加载
    task_db.clear()
    print(f"清空后: {len(list_tasks())} 个")
    load_tasks()
    print(f"加载后: {len(list_tasks())} 个")

    # 安全删除
    try:
        safe_delete_task(9999)
        print("❌ 应该抛异常但没有")
    except TaskNotFoundError as e:
        print(f"✅ 正确抛出异常: {e.message}")

    print("\n✅ Day 5 综合 CRUD 完成！")
