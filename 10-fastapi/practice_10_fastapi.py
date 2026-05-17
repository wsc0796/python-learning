"""
10 — FastAPI 练习
运行前：pip install fastapi uvicorn
运行：uvicorn practice_10_fastapi:app --reload
然后浏览器打开 http://127.0.0.1:8000/docs
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# ============================================================
# TODO 1: 创建 FastAPI 实例
# ============================================================
# app = ...


# ============================================================
# TODO 2: 定义 Item 模型
# ============================================================
# name: str, price: float (>0), stock: int (>=0, 默认0)

class Item(BaseModel):
    # 你的代码...
    pass


# ============================================================
# TODO 3: 根路由
# ============================================================
# @app.get("/")
# def root():
#     return {"message": "FastAPI 已启动"}


# ============================================================
# TODO 4: 路径参数
# ============================================================
# GET /items/{item_id} → 返回 {"item_id": item_id}
# item_id 是 int 类型


# ============================================================
# TODO 5: 查询参数
# ============================================================
# GET /items → 接收 q: str = "all", skip: int = 0, limit: int = 10
# 返回 {"q": q, "skip": skip, "limit": limit}


# ============================================================
# TODO 6: POST 用 Pydantic 校验
# ============================================================
# POST /items
# 接收 Item 模型，返回 {"received": item}


# ============================================================
# TODO 7: 完整的 Task CRUD（衔接 Day 5）
# ============================================================
# 把昨天的 CRUD 搬到 FastAPI 里
# task_db: dict[int, dict] = {}
# next_id: int = 1
#
# POST /tasks → 创建
# GET /tasks → 列表
# GET /tasks/{id} → 查单个（不存在抛 404）
# DELETE /tasks/{id} → 删除（不存在抛 404）


if __name__ == "__main__":
    print("""
    运行方式：
    uvicorn practice_10_fastapi:app --reload
    然后打开 http://127.0.0.1:8000/docs
    """)
