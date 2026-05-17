---
aliases:
  - 10-fastapi
---
# 10 — FastAPI 入门（对照 Spring Boot）

> 相关笔记：[综合 CRUD](../09-crud/theory_09_crud.md) · [Pydantic 数据校验](../07-pydantic/theory_07_pydantic.md)

## 环境准备

```bash
pip install fastapi uvicorn
```

## 1. 最小的 FastAPI 应用

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

运行：
```bash
uvicorn main:app --reload
# 访问 http://127.0.0.1:8000
# 自动文档 http://127.0.0.1:8000/docs
```

---

## 2. 路由对照 Spring Boot

| Spring Boot | FastAPI |
|------------|---------|
| `@RestController` | `app = FastAPI()` |
| `@GetMapping("/items")` | `@app.get("/items")` |
| `@PostMapping("/items")` | `@app.post("/items")` |
| `@PathVariable Long id` | `id: int`（路径参数） |
| `@RequestParam String q` | `q: str`（查询参数） |
| `@RequestBody DTO dto` | `dto: DTO`（自动用 Pydantic 校验） |

---

## 3. 路径参数

```python
# Java: @GetMapping("/items/{id}")  @PathVariable Long id
@app.get("/items/{item_id}")
def read_item(item_id: int):          # 自动解析路径参数并转为 int
    return {"item_id": item_id}
```

---

## 4. 查询参数

```python
# Java: @RequestParam(required=false, default="all")
@app.get("/items")
def list_items(q: str = "all", skip: int = 0, limit: int = 10):
    return {"query": q, "skip": skip, "limit": limit}
```

**规则：**
- 路径参数 = 路径里的 `{id}` → 同名函数参数
- 查询参数 = 不在路径里的其他参数 → URL 上 `?q=xxx&skip=0`
- 有默认值 = 可选参数，没有默认值 = 必填

---

## 5. Pydantic 做请求体验证

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    stock: int = 0

# Java: @PostMapping("/items")  @RequestBody ItemDTO dto  @Valid
@app.post("/items")
def create_item(item: Item):         # FastAPI 自动用 Pydantic 校验
    return item                      # 自动转 JSON
```

---

## 6. 响应模型

```python
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    # ...
    return item_response_data
```

---

## 7. 完整的 CRUD 示例

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    priority: int = 3

class TaskResponse(Task):
    id: int
    completed: bool = False

db: dict[int, dict] = {}
next_id = 1

@app.post("/tasks", response_model=TaskResponse)
def create(task: Task):
    global next_id
    item = {"id": next_id, **task.model_dump(), "completed": False}
    db[next_id] = item
    next_id += 1
    return item

@app.get("/tasks")
def list_tasks():
    return list(db.values())

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="任务不存在")
    return db[task_id]
```

---

## 启动和测试

```bash
# 启动
uvicorn 文件名:app --reload

# 访问自动文档
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
```

---

## 对照 Java 关键差异

| 概念 | Spring Boot | FastAPI |
|------|------------|---------|
| 启动类 | `@SpringBootApplication` | `app = FastAPI()` |
| 路由 | `@GetMapping` | `@app.get` |
| 参数校验 | `@Valid` + 注解 | Pydantic + 类型提示 |
| 文档 | Swagger 需配置 | http://localhost:8000/docs 自动生成 |
| 依赖注入 | `@Autowired` | `Depends()` |
| 运行 | Maven/Gradle 构建 | uvicorn 直接启动 |
