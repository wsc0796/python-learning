---
aliases:
  - 17-context-iterator-async
---
# 从装饰器到异步：三个必须补的 Python 基础

> 前置：装饰器已掌握、with open 会用但不懂原理、yield 见过但没系统学过、async 完全没接触
> 目标：补齐上下文管理器 → 迭代器/生成器 → async/await，为 FastAPI 实战和 AI Agent 开发铺路
> 用时：约 6 天（每天 30-40 分钟）

---

## 为什么学这个专题

你刚学完装饰器，已经理解了"函数可以包装函数"。接下来这三块知识是 Python 进阶开发的共同基础：

1. **上下文管理器** — `with` 底层原理 + `@contextmanager`（装饰器的直接应用）
2. **迭代器/生成器** — `yield` 的暂停/恢复机制（异步协程的底层基础）
3. **async/await** — FastAPI 路由 + LLM API 调用 + AI Agent 并发

```
装饰器 ──→ @contextmanager ──→ 上下文管理器
                │
                └──→ 生成器(yield) ──→ 协程基础
                                            │
                ┌───────────────────────────┘
                ↓
          async/await ──→ FastAPI / AI Agent
```

## 学习顺序（按天）

| 天 | 内容 | 核心问题 |
|----|------|---------|
| 1 | [[01-context-manager]] | `with open()` 背后发生了什么？ |
| 2 | [[02-iterator-generator]] 上半 | `for` 循环底层怎么工作？ |
| 3 | [[02-iterator-generator]] 下半 | `yield` 为什么能暂停函数？ |
| 4 | [[03-async-await]] 上半 | `async def` 和普通 `def` 有什么区别？ |
| 5 | [[03-async-await]] 下半 | 如何并发执行多个 IO 任务？ |
| 6 | [[04-mini-projects]] | 把三个知识点串起来 |

## 学完后的能力

- 解释 `with open(...) as f` 的完整执行流程
- 手写支持 `with` 的类，手写 `@contextmanager` 函数
- 手写迭代器类 + 生成器函数，理解 `yield from`
- 写 `async def` 函数，用 `asyncio.gather()` 并发执行
- 理解为什么 FastAPI 路由是 `async def`，为什么 AI Agent 需要异步

## 相关笔记

- [[11-closure-decorator]] — 装饰器（`@contextmanager` 的基础）
- [[03-file-exception]] — `with open` 你已经天天在用了
- [[16-python-gaps]] — yield 基础（P2 标记的内容现在升到 P1）
- [[10-fastapi]] — `async def` 路由落地场景
