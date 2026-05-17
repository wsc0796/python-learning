---
aliases:
  - 09-crud
---
# 09 — 综合 CRUD（阶段一收尾）

> 相关笔记：[文件读写与异常](../03-file-exception/theory_03_file_exception.md) · [FastAPI 入门](../10-fastapi/theory_10_fastapi.md)

## 目标

把 Day 3（Pydantic）+ Day 4（类型提示/DI）+ 文件操作用一个项目串起来。

## 架构

```
09-crud/
├── practice_09_crud.py    ← 练习文件，你要改这个
├── tasks.json             ← 运行后自动生成（持久化）
```

## 我们要做什么

一个**内存 Task 管理系统**：

```
功能：
├── list_tasks()         → 列出所有任务
├── create_task()        → 创建新任务
├── complete_task()      → 标记完成
├── delete_task()        → 删除任务  
└── save/load_tasks()    → 文件持久化
```

## 数据流

```
用户调用 → CRUD 函数 → Pydantic 校验 → 操作 dict 数据库 → 返回结果
                                                         ↓
                                                   可保存到 JSON 文件
```

## 你需要用的知识

| 知识点 | 出处 | 怎么用 |
|--------|------|--------|
| Pydantic BaseModel + Field | Day 3 = 07-pydantic | 校验任务数据 |
| 类型提示 | 05-module-types | 函数签名清晰 |
| 文件读写 | 03-file-exception | JSON 存/读 |
| 异常处理 | 03-file-exception | 任务不存在时抛异常 |
| 列表推导式 | 04-listcomp | 筛选任务 |

## 完成后你就能

看懂 FastAPI 项目里 `models.py`（Pydantic）+ `service.py`（CRUD）的结构。
