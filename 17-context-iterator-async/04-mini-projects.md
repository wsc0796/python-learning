---
aliases:
  - 04-mini-projects
---
# 04. Mini Projects：把三个知识点串起来

> 前置：已读完 01-03
> 目标：用 3 个小项目把上下文管理器、生成器、异步串成应用
> 用时：约 30 分钟（3 个项目）

---

## 项目一：计时器上下文管理器

### 目标

用 `@contextmanager` 实现一个可以嵌套的计时器。

### 代码

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name="任务"):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        indent = "  " * timer._level
        timer._level -= 1
        print(f"{indent}⏱ {name}: {elapsed:.3f}s")

timer._level = 0

@contextmanager
def timed_block(name):
    timer._level += 1
    with timer(name):
        yield
```

使用：

```python
with timed_block("外层"):
    time.sleep(0.5)
    with timed_block("内层1"):
        time.sleep(0.3)
    with timed_block("内层2"):
        time.sleep(0.2)

# ⏱ 内层2: 0.201s
#   ⏱ 内层1: 0.301s
# ⏱ 外层: 1.007s
```

### 涉及知识

- `@contextmanager`
- `try...finally`
- `with` 嵌套

---

## 项目二：分页数据生成器

### 目标

用生成器模拟"分页从 API 拉数据"——每次 yield 一页，内存常驻的只有当前页。

### 代码

```python
def fetch_pages(total, page_size):
    """模拟分页获取数据"""
    page = 0
    while page * page_size < total:
        start = page * page_size
        end = min(start + page_size, total)
        # 模拟：实际场景这里是 requests.get(f"?page={page}")
        page_data = [f"item_{i}" for i in range(start, end)]
        yield page_data
        page += 1

# 使用
for page_num, page_data in enumerate(fetch_pages(100, 15), start=1):
    print(f"第{page_num}页: {len(page_data)}条 ({page_data[0]}..{page_data[-1]})")

# 输出:
# 第1页: 15条 (item_0..item_14)
# 第2页: 15条 (item_15..item_29)
# ...
# 第7页: 10条 (item_90..item_99)
```

### 和 list 方式的对比

```python
# ❌ 全量加载：10000条 → 内存爆炸
all_data = fetch_all_items()
for page in split_into_pages(all_data, 15):
    process(page)

# ✅ 惰性生成：不管多少条，内存只有当前页
for page in fetch_pages(10000, 15):
    process(page)
```

---

## 项目三：异步批量请求模拟器

### 目标

用 `asyncio.gather` 模拟同时请求多个 URL，对比同步方案的时间差。

### 代码

```python
import asyncio
import time

async def fetch_url(url):
    """模拟 HTTP 请求"""
    print(f"  开始请求 {url}")
    await asyncio.sleep(1.5)   # 模拟网络延迟
    print(f"  完成 {url}")
    return f"<html from {url}>"

# ===== 同步版 =====
def sync_main(urls):
    print("\n=== 同步模式 ===")
    start = time.time()
    for url in urls:
        # 同步写法：逐次等待
        pass  # 你没法直接调 async 函数，这里只是示意
    # 总耗时 = 1.5 * 5 = 7.5s

# ===== 异步并发版 =====
async def async_main():
    print("\n=== 异步并发模式 ===")
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments",
        "https://api.example.com/tags",
        "https://api.example.com/status",
    ]

    start = time.time()
    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    elapsed = time.time() - start

    print(f"\n请求 {len(urls)} 个 URL")
    print(f"并发总耗时: {elapsed:.2f}s")
    print(f"如果同步: {1.5 * len(urls):.1f}s")
    return results

asyncio.run(async_main())
```

**预期输出**：5 个 URL 并发总耗时约 1.5 秒（同步需要 7.5 秒）。

---

## 项目四（选做）：迷你 Agent 工具调用

### 场景

模拟一个 Agent 同时调用搜索工具、数据库工具、LLM 总结工具。

### 代码

```python
import asyncio

async def search_tool(query: str) -> str:
    await asyncio.sleep(1.0)   # 模拟搜索引擎 API
    return f"搜索结果: 找到和'{query}'相关的3个网页"

async def db_tool(user_id: str) -> str:
    await asyncio.sleep(0.5)   # 模拟数据库查询
    return f"用户{user_id}: 偏好=Python, 历史=5次对话"

async def llm_summarize(text: str) -> str:
    await asyncio.sleep(1.5)   # 模拟 LLM API 调用
    return f"LLM总结: 该用户是Python初学者，对AI方向感兴趣"

async def agent_run(user_query: str, user_id: str):
    """Agent 主流程：并发调用工具，汇总后调 LLM"""
    print(f"\n🤖 Agent 开始处理: {user_query}")

    # 第一步：并发调用搜索和数据库（这两个互不依赖）
    search_result, db_result = await asyncio.gather(
        search_tool(user_query),
        db_tool(user_id),
    )

    # 第二步：用汇总结果调 LLM
    final_answer = await llm_summarize(
        f"问题: {user_query}\n{search_result}\n{db_result}"
    )

    print(f"📝 {final_answer}")
    return final_answer

# 运行
asyncio.run(agent_run("如何学习异步编程", "user_001"))
```

### 这里体现的设计思想

```
         search_tool ──┐
                        ├── gather（并发等待）──→ llm_summarize ──→ 最终回答
         db_tool ──────┘
```

**互不依赖的 IO 任务 → 用 `gather` 并发。有依赖的任务 → 顺序 `await`。**

这和 Hello-Agents 教程里的 Agent 工作流是同一种模式。
