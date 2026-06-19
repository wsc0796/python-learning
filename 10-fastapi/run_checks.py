"""
最小自检脚本。

不启动 uvicorn，直接用 TestClient 模拟 HTTP 请求，自动验证所有接口。
运行：
    python run_checks.py
"""

from pathlib import Path

from fastapi.testclient import TestClient

import dependencies
from main import app


def main() -> None:
    # 需求①：清空旧数据，确保每次测试从干净状态开始
    if dependencies.DATA_FILE.exists():
        dependencies.DATA_FILE.unlink()

    # 需求②：创建测试客户端（模拟 HTTP 请求，不启动真实服务器）
    client = TestClient(app)

    # 需求③：测试根路由 —— 服务是否启动
    assert client.get("/").status_code == 200

    # 需求④：测试创建任务 —— POST /tasks
    created = client.post("/tasks", json={"title": "学习 Pydantic", "priority": 1})
    assert created.status_code == 201, created.text       # 创建成功
    task = created.json()                                  # 拿到响应 JSON
    task_id = task["id"]                                   # 记下 id 给后面用

    # 需求⑤：验证返回的数据 —— title 原样返回，completed 默认 false
    assert task["title"] == "学习 Pydantic"
    assert task["completed"] is False

    # 需求⑥：测试查看全部 —— GET /tasks
    listed = client.get("/tasks")
    assert listed.status_code == 200
    assert len(listed.json()) == 1                         # 刚创建了 1 条

    # 需求⑦：测试标记完成 —— PATCH /tasks/{id}/complete
    completed = client.patch(f"/tasks/{task_id}/complete")
    assert completed.status_code == 200
    assert completed.json()["completed"] is True           # 状态变成了已完成

    # 需求⑧：测试按完成状态筛选 —— GET /tasks?completed=true
    filtered = client.get("/tasks?completed=true")
    assert filtered.status_code == 200
    assert len(filtered.json()) == 1                       # 有 1 条已完成的

    # 需求⑨：测试 404 错误 —— 查不存在的任务应返回 404
    missing = client.get("/tasks/999")
    assert missing.status_code == 404

    # 需求⑩：测试删除 —— DELETE /tasks/{id}
    deleted = client.delete(f"/tasks/{task_id}")
    assert deleted.status_code == 204                      # 删除成功，无返回内容

    print("all checks passed")


if __name__ == "__main__":
    main()
