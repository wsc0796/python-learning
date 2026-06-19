---
aliases:
  - 03-async-await
---
# 03. async/await：异步编程

> 前置：理解 yield 的暂停/恢复、会用 FastAPI 基本路由
> 目标：写 `async def` 函数，用 `asyncio.gather()` 并发执行 IO 任务，理解为什么 AI Agent 需要异步
> 用时：约 25 分钟（分两次读：上半=基础概念，下半=并发实战）
>
> 相关笔记：[[02-iterator-generator]] · [[10-fastapi]] · [[13-multithreading]]

---

## Part A：为什么需要异步

### 一、同步的痛

```python
import time

def download(name):
    print(f"开始下载 {name}")
    time.sleep(2)           # 模拟网络等待
    print(f"下载完成 {name}")

# 顺序执行三个下载
download("A")   # 等 2 秒
download("B")   # 等 2 秒
download("C")   # 等 2 秒
# 总耗时: 6 秒 — CPU 95% 的时间在傻等
```

**问题**：网络/数据库/文件 IO 占的时间远多于 CPU 计算。等待期间 CPU 完全可以做别的事。

### 二、异步的思路

```
同步：          异步：
A →→→→ A完成    A →→→→→→→→ A完成
  B →→→→ B完成   B →→→→→→→→ B完成
    C →→→→ C完成   C →→→→→→ C完成
────────────    ────────────
  6 秒              ~2 秒
```

**异步不是让单个任务变快，而是让多个任务的等待时间重叠。**

---

## Part B：基础概念

### 三、核心术语

| 术语 | 一句话 | 类比 |
|------|--------|------|
| **协程 (coroutine)** | `async def` 定义的函数 | 一个可以被暂停和恢复的任务 |
| **await** | 等待一个协程完成，等待期间交出控制权 | "你去做别的，好了叫我" |
| **事件循环 (event loop)** | 调度所有协程的"管家" | 操作系统里的调度器 |
| **Task** | 被事件循环管理的协程 | 排进调度队列的任务单 |

### 四、第一个 async 程序

```python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)    # ← 注意：是 asyncio.sleep，不是 time.sleep
    print("World")

asyncio.run(hello())
```

关键点：
- `async def` 定义的函数**调用后不立即执行**——返回一个 coroutine 对象
- `asyncio.run()` 是入口：创建事件循环 → 运行协程 → 关闭循环
- `asyncio.sleep()` **不阻塞事件循环**，`time.sleep()` 会阻塞

### 五、await 做了什么

```python
async def fetch_data():
    print("开始请求...")
    await asyncio.sleep(2)     # ← 在这里暂停，把控制权交还给事件循环
    print("数据到了！")
    return {"result": "ok"}
```

**`await` = "我要等这个东西完成，但我等的时候你可以去干别的"**。

`await` 后面必须跟一个 **awaitable 对象**（协程、Task、Future）。

---

## Part C：并发实战

### 六、顺序 await（不是并发！）

```python
async def download(name):
    print(f"开始 {name}")
    await asyncio.sleep(2)
    print(f"完成 {name}")

async def main():
    await download("A")   # 等 A 完成
    await download("B")   # 等 B 完成
    await download("C")   # 等 C 完成

asyncio.run(main())
# 总耗时: 约 6 秒   ← 虽然是 async，但顺序 await = 没并发
```

**`async def` 本身不等于并发。必须显式创建并发任务。**

### 七、`create_task` — 真正的并发

```python
async def main():
    task_a = asyncio.create_task(download("A"))
    task_b = asyncio.create_task(download("B"))
    task_c = asyncio.create_task(download("C"))

    # 三个任务已经在跑了，现在等待它们全部完成
    await task_a
    await task_b
    await task_c

asyncio.run(main())
# 总耗时: 约 2 秒   ← 三个任务并发执行
```

**`create_task()` = 把协程注册到事件循环，让它"在后台"运行。**

### 八、`gather` — 更优雅的并发

```python
async def main():
    results = await asyncio.gather(
        download("A"),
        download("B"),
        download("C"),
    )
    print(results)  # ['A done', 'B done', 'C done']

asyncio.run(main())
```

`gather` 同时做三件事：
1. 把所有协程注册为 Task
2. 并发执行
3. 等全部完成后，按传入顺序返回结果列表

### 九、异步异常处理

```python
async def risky_task(name):
    await asyncio.sleep(1)
    if name == "B":
        raise ValueError(f"{name} 失败了")
    return f"{name} 成功"

async def main():
    try:
        results = await asyncio.gather(
            risky_task("A"),
            risky_task("B"),   # 这个会失败
            risky_task("C"),
        )
    except ValueError as e:
        print(f"捕获到: {e}")
    # A 和 C 的结果呢？gather 默认：一个失败 → 全部抛异常

asyncio.run(main())
```

如果需要"部分失败不影响其他"：`gather(..., return_exceptions=True)`，异常会作为结果元素返回。

---

## Part D：和你的方向连接

### 十、FastAPI 中的 async def

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await db.fetch_user(user_id)    # 异步查数据库
    posts = await db.fetch_posts(user_id)  # 异步查帖子
    return {"user": user, "posts": posts}
```

FastAPI 框架本身就是基于 asyncio 的。路由函数用 `async def` 意味着：
- 等待数据库时，服务器可以处理其他请求
- 不会因为一个慢请求卡住整个服务

### 十一、AI Agent 中为什么需要异步

典型 Agent 的一次执行可能涉及：

```python
async def agent_run(task: str):
    # 同时调用多个工具
    search_result, db_result, memory = await asyncio.gather(
        search_tool(task),         # 搜索（网络 IO）
        db_tool(task),             # 数据库（数据库 IO）
        memory_tool(task),         # 记忆检索（数据库 IO）
    )

    # 用汇总的结果调 LLM
    answer = await llm_call(task, search_result, db_result, memory)
    return answer
```

**Agent 调用 LLM API 是最典型的 IO 等待场景**——发一个请求，等 1-5 秒拿回复。同步写的话，Agent 每一步都在干等；异步写的话，多个工具调用可以同时发出。

---

## 十二、适合/不适合异步的场景

| 适合（IO 密集型） | 不适合（CPU 密集型） |
|-------------------|---------------------|
| HTTP 请求 | 大量数学运算 |
| 数据库查询 | 图像/视频处理 |
| 文件读写 | 模型训练 |
| LLM API 调用 | 数据加密/解密 |
| 多个 Agent 协作 | 纯计算的算法题 |

CPU 密集型 → 考虑多进程（`multiprocessing`）或 C 扩展。

---

## 十三、常见易错点

| 易错点 | 说明 |
|--------|------|
| 调用 `async def` 函数不加 `await` | 得到 coroutine 对象，函数体不会执行 |
| 在 async 函数里用 `time.sleep` | 阻塞事件循环！用 `await asyncio.sleep` |
| 以为 `async def` 就是并行 | async 是**并发**（交替执行），不是**并行**（同时执行） |
| 顺序写多个 `await` | 没有并发效果，只是普通顺序执行 |
| 忘记 `asyncio.run()` | 顶层入口必须用 `asyncio.run()`，不能直接调 async 函数 |
| CPU 密集任务用 asyncio | 不会加速，反而因为线程切换更慢 |
