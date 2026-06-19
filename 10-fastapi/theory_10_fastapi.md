---
aliases:
  - 10-fastapi
---
# 10 — FastAPI 入门：从零理解一个接口怎么工作

> 相关笔记：[综合 CRUD](../09-crud/theory_09_crud.md) · [Pydantic 数据校验](../07-pydantic/theory_07_pydantic.md) · [类型提示与 DI](../08-typing-di/theory_08_typing_di.md) · [课堂老师函数程序对照](../00-学习路线/课堂老师程序-函数专题对照.md) · [[00-学习路线/课堂程序4-异常专题对照|课堂程序4：异常专题对照]]

这章先不追求“背会所有语法”，而是先建立一条主线：

```text
用户发 HTTP 请求
→ FastAPI 根据路由找到函数
→ 函数参数接收数据
→ Pydantic 校验请求体
→ 你的函数处理业务
→ return 的内容变成 JSON 响应
```

如果你只记一句话：

> FastAPI 就是把“HTTP 请求”翻译成“Python 函数调用”的框架。

---

## 0. 学 FastAPI 前需要知道什么

你不需要一开始就懂很多后端知识，但下面这些概念必须慢慢补起来：

| 基础 | 为什么需要 |
|------|------------|
| 函数 | 一个接口本质上就是一个函数 |
| 字典 `dict` | FastAPI 返回的 JSON 很像 Python 字典 |
| 类型提示 | `item_id: int` 告诉 FastAPI 怎么转换参数 |
| Pydantic | 校验请求体，比如 `content` 不能为空 |
| 文件读写 | 小项目会用 JSON 文件模拟数据库 |
| 异常 | 找不到数据时要返回 404 |
| 装饰器 | `@app.get()` 就是把函数注册成接口 |

你现在看不懂 FastAPI，很多时候不是 FastAPI 难，而是这些前置知识还没完全连起来。

---

## 1. 环境准备

安装：

```bash
pip install fastapi uvicorn
```

这两个东西分工不同：

| 工具 | 作用 |
|------|------|
| `fastapi` | 写接口的框架 |
| `uvicorn` | 把 FastAPI 应用跑起来的服务器 |

类比 Java：

| Java / Spring Boot | Python / FastAPI |
|--------------------|------------------|
| Spring Boot 框架 | FastAPI 框架 |
| Tomcat / 内置 Web 容器 | Uvicorn |

---

## 2. 最小 FastAPI 应用

文件名假设叫 `main.py`：

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
```

访问：

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

逐行理解：

```python
from fastapi import FastAPI
```

导入 FastAPI 这个类。

```python
app = FastAPI()
```

创建一个 FastAPI 应用对象。后面所有接口都挂在这个 `app` 上。

```python
@app.get("/")
```

把下面的 `root()` 函数注册成一个 GET 接口，路径是 `/`。

```python
def root():
    return {"message": "Hello World"}
```

当浏览器访问 `/` 时，FastAPI 会调用这个函数，并把返回的字典转换成 JSON。

---

## 3. `uvicorn main:app --reload` 是什么意思

```bash
uvicorn main:app --reload
```

拆开看：

| 部分 | 含义 |
|------|------|
| `uvicorn` | 用 Uvicorn 启动服务 |
| `main` | 文件名 `main.py`，不写 `.py` |
| `app` | 文件里的 `app = FastAPI()` 这个变量 |
| `--reload` | 代码改了自动重启，开发时常用 |

如果你的文件叫 `server.py`，里面也是 `app = FastAPI()`，启动命令就是：

```bash
uvicorn server:app --reload
```

---

## 4. 路由是什么

路由就是：

```text
哪个 URL + 哪种 HTTP 方法 → 交给哪个 Python 函数处理
```

比如：

```python
@app.get("/notes")
def list_notes():
    return []
```

意思是：

```text
GET /notes 这个请求来了
→ FastAPI 调用 list_notes()
→ 函数 return 什么，用户就收到什么
```

对照 Spring Boot：

| Spring Boot | FastAPI |
|------------|---------|
| `@RestController` | `app = FastAPI()` |
| `@GetMapping("/items")` | `@app.get("/items")` |
| `@PostMapping("/items")` | `@app.post("/items")` |
| `@DeleteMapping("/items/{id}")` | `@app.delete("/items/{id}")` |

---

## 5. GET 和 POST 的区别

先用最简单的方式记：

| 方法 | 常见用途 | 例子 |
|------|----------|------|
| `GET` | 查询数据 | 查看全部笔记、查看某条笔记 |
| `POST` | 新增数据 | 创建一条笔记 |
| `PATCH` | 修改部分数据 | 把任务标记完成、修改笔记内容 |
| `DELETE` | 删除数据 | 删除一条笔记 |

比如笔记项目：

```text
GET    /notes       查看全部笔记
POST   /notes       创建笔记
GET    /notes/1     查看 id=1 的笔记
PATCH  /notes/1     修改 id=1 的笔记
DELETE /notes/1     删除 id=1 的笔记
```

---

## 6. 路径参数：从 URL 路径里拿值

代码：

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

访问：

```text
GET /items/10
```

FastAPI 会做这件事：

```text
URL 里的 10
→ 找到 {item_id}
→ 转成 int
→ 传给函数参数 item_id
```

所以函数实际相当于被这样调用：

```python
read_item(item_id=10)
```

如果你访问：

```text
GET /items/abc
```

因为 `abc` 不能转成 `int`，FastAPI 会返回 `422 Validation Error`。

对照 Java：

```java
@GetMapping("/items/{id}")
public Item getItem(@PathVariable Long id) { ... }
```

FastAPI 写法：

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    ...
```

---

## 7. 查询参数：从问号后面拿值

代码：

```python
@app.get("/items")
def list_items(q: str = "all", skip: int = 0, limit: int = 10):
    return {"query": q, "skip": skip, "limit": limit}
```

访问：

```text
GET /items?q=book&skip=0&limit=5
```

FastAPI 会把问号后面的参数传给函数：

```python
list_items(q="book", skip=0, limit=5)
```

规则：

| 情况 | FastAPI 怎么判断 |
|------|------------------|
| 写在路径 `{item_id}` 里 | 路径参数 |
| 没写在路径里，但出现在函数参数里 | 查询参数 |
| 有默认值 | 可选 |
| 没有默认值 | 必填 |

例子：

```python
def list_items(q: str, limit: int = 10):
    ...
```

这里：

```text
q 必填
limit 可选，不传默认是 10
```

---

## 8. 请求体：POST 时传 JSON

如果要创建商品，前端或 Swagger 会发这样的 JSON：

```json
{
  "name": "鼠标",
  "price": 99.9,
  "stock": 10
}
```

FastAPI 需要知道这个 JSON 应该长什么样，所以要先定义 Pydantic 模型：

```python
from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)
```

然后在接口函数里使用它：

```python
@app.post("/items")
def create_item(item: ItemCreate):
    return item
```

这句：

```python
def create_item(item: ItemCreate):
```

意思是：

```text
请求体里的 JSON
→ 用 ItemCreate 的规则校验
→ 校验成功后变成 item 对象
→ 传给 create_item 函数
```

如果用户传：

```json
{
  "name": "",
  "price": -1,
  "stock": 10
}
```

FastAPI 会返回 `422`，因为：

```text
name 长度不能小于 1
price 必须大于 0
```

---

## 9. 返回值：为什么 `return` 有用

在普通 Python 函数里：

```python
def add(a, b):
    return a + b
```

`return` 是把结果交给调用者。

在 FastAPI 里：

```python
@app.get("/hello")
def hello():
    return {"message": "hi"}
```

调用者不是你手写的代码，而是 FastAPI。

流程是：

```text
浏览器 / Swagger 发请求
→ FastAPI 调用 hello()
→ hello() return 一个 dict
→ FastAPI 把 dict 转成 JSON
→ 返回给浏览器 / Swagger
```

所以：

```python
return service.create_note(note)
```

意思是：

```text
service 创建出一条笔记
→ 把这条笔记 return 给 FastAPI
→ FastAPI 把它变成 HTTP 响应
→ 用户在 Swagger 里看到结果
```

---

## 10. 响应模型：`response_model` 是出口规则

看这个接口：

```python
@app.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate):
    return item_data
```

`response_model=ItemRead` 的意思是：

```text
不管函数里面 return 了什么
最终返回给用户之前
都要按 ItemRead 的格式整理一遍
```

例子：

```python
class ItemCreate(BaseModel):
    name: str
    price: float


class ItemRead(ItemCreate):
    id: int
```

创建时，用户只需要传：

```json
{
  "name": "鼠标",
  "price": 99.9
}
```

返回时，用户应该看到：

```json
{
  "id": 1,
  "name": "鼠标",
  "price": 99.9
}
```

所以：

| 模型 | 作用 |
|------|------|
| `ItemCreate` | 入口规则：用户创建时要传什么 |
| `ItemRead` | 出口规则：接口返回时长什么样 |

对你的 notes-api 来说：

| 模型 | 作用 |
|------|------|
| `NoteCreate` | 创建笔记，只需要 `content` |
| `NoteUpdate` | 修改笔记，`content` 可以不传 |
| `NoteRead` | 返回笔记，包含 `id`、`content`、`created_at` |

---

## 11. 状态码：告诉用户请求结果

HTTP 状态码就是接口处理结果的“数字说明”。

常见状态码：

| 状态码 | 含义 | 常见场景 |
|--------|------|----------|
| `200` | 成功 | 查询成功 |
| `201` | 创建成功 | POST 新增成功 |
| `204` | 删除成功但没有响应体 | DELETE 成功 |
| `404` | 资源不存在 | id 找不到 |
| `422` | 请求数据格式不对 | 类型错、必填字段没传、字段不符合约束 |
| `500` | 服务器内部错误 | 代码异常 |

例子：

```python
from fastapi import status


@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    ...
```

这里的意思是：

```text
创建成功时返回 201
```

---

## 12. 404 和 422 的区别

这两个你在 Swagger 里经常会看到。

| 错误 | 谁发现的 | 含义 |
|------|----------|------|
| `422` | FastAPI / Pydantic | 请求数据不合法，函数可能还没真正执行 |
| `404` | 你的业务代码 | 请求格式没问题，但要找的数据不存在 |

例子 1：访问

```text
GET /notes/abc
```

如果代码要求：

```python
note_id: int
```

`abc` 不能转成整数，所以是 `422`。

例子 2：访问

```text
GET /notes/999
```

`999` 是合法整数，FastAPI 会调用你的函数。但 service 发现没有这条笔记，所以你返回 `404`。

一句话：

```text
422 = 请求数据不对
404 = 数据不存在
```

---

## 13. HTTPException：把业务错误翻译成 HTTP 错误

代码：

```python
from fastapi import HTTPException


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    note = service.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="笔记不存在")
    return note
```

`raise HTTPException(...)` 的意思是：

```text
不要正常返回数据了
直接告诉用户：这次请求失败，状态码是 404，原因是“笔记不存在”
```

在分层项目里，通常是：

```text
service.py 抛出业务异常 NoteNotFoundError
main.py 捕获异常
main.py 把它翻译成 HTTPException(404)
```

这样可以保持分工清楚：

| 文件 | 负责什么 |
|------|----------|
| `service.py` | 知道“笔记不存在”这个业务事实 |
| `main.py` | 知道 HTTP 应该返回 404 |

---

## 14. 一个内存版 CRUD 示例

这个例子先不用文件、数据库，只用一个字典模拟存储。

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(default=3, ge=1, le=5)


class TaskRead(TaskCreate):
    id: int
    completed: bool = False


db: dict[int, dict] = {}
next_id = 1


@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "priority": task.priority,
        "completed": False,
    }

    db[next_id] = new_task
    next_id += 1

    return new_task


@app.get("/tasks", response_model=list[TaskRead])
def list_tasks():
    return list(db.values())


@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="任务不存在")

    return db[task_id]
```

这段代码的核心流程：

```text
POST /tasks
→ 请求体 JSON 用 TaskCreate 校验
→ 生成 id 和 completed
→ 存进 db
→ 按 TaskRead 格式返回
```

---

## 15. 分层项目里 main.py 应该做什么

在真正项目里，不建议把所有代码都写在 `main.py`。

你的 notes-api 分层应该是：

```text
models.py        数据形状：NoteCreate / NoteUpdate / NoteRead
repository.py    存储：读写 notes.json
service.py       业务：创建、查询、修改、删除
dependencies.py  组装：创建 repository 和 service
main.py          HTTP：路由、状态码、错误翻译
```

`main.py` 只做翻译：

```text
HTTP 请求
→ 调用 service
→ 把 service 的结果变成 HTTP 响应
```

它不应该关心：

```text
notes.json 怎么读写
id 怎么生成
文件夹怎么创建
json.dump 怎么写
```

这些应该放在 `repository.py` 或 `service.py`。

---

## 16. Depends：让 FastAPI 帮你拿对象

先看不使用依赖注入的写法：

```python
@app.get("/notes")
def list_notes():
    service = NoteService(...)
    return service.list_notes()
```

问题是：

```text
每个接口都要自己创建 service
代码重复
以后换实现很麻烦
测试也不好替换
```

所以我们把创建对象放到 `dependencies.py`：

```python
def get_note_service() -> NoteService:
    return note_service
```

然后在接口里写：

```python
from typing import Annotated
from fastapi import Depends

NoteServiceDep = Annotated[NoteService, Depends(get_note_service)]


@app.get("/notes")
def list_notes(service: NoteServiceDep):
    return service.list_notes()
```

意思是：

```text
这个 service 参数不是用户传的
FastAPI 看到 Depends(get_note_service)
→ 自动调用 get_note_service()
→ 把返回值塞给 service 参数
```

你可以把它理解成：

```text
Depends = 取货说明
get_note_service = 取货口
service 参数 = 拿到的货
```

---

## 17. 对照 Java / Spring Boot

| 概念         | Spring Boot              | FastAPI                     |
| ---------- | ------------------------ | --------------------------- |
| 应用入口       | `@SpringBootApplication` | `app = FastAPI()`           |
| Controller | `@RestController`        | 写在 `main.py` 或 router 里     |
| GET 接口     | `@GetMapping`            | `@app.get`                  |
| POST 接口    | `@PostMapping`           | `@app.post`                 |
| 路径参数       | `@PathVariable Long id`  | `id: int`                   |
| 查询参数       | `@RequestParam`          | 普通函数参数                      |
| 请求体        | `@RequestBody DTO dto`   | `dto: PydanticModel`        |
| 参数校验       | `@Valid` + 注解            | Pydantic + `Field`          |
| 依赖注入       | `@Autowired` / 构造器注入     | `Depends()`                 |
| 接口文档       | Swagger 配置               | `/docs` 自动生成                |
| 启动         | Maven/Gradle             | `uvicorn main:app --reload` |

---

## 18. 新手自检清单

学完这一章，你不需要背代码，但要能回答：

- [ ] `app = FastAPI()` 是干什么的？ 启动 ***应用入口*
- [ ] `@app.get("/notes")` 是干什么的？  注册路由
- [ ] `def get_note(note_id: int)` 里的 `note_id` 从哪里来？ depency层依赖注入
- [ ] 查询参数和路径参数有什么区别？ 不知道
- [ ] POST 请求体为什么要用 Pydantic 模型？ 为了校验数据
- [ ] `response_model=NoteRead` 是入口规则还是出口规则？ 出口
- [ ] `return service.create_note(note)` 的结果最后去了哪里？ 不知道  
- [ ] 422 和 404 的区别是什么？不知道
- [ ] `Depends(get_note_service)` 在请求的哪一步发生？不知道
- [ ] `main.py` 为什么不应该直接 `json.load()`？ 不知道

如果这些能说清楚，你就不是在死记 FastAPI 语法，而是真的开始建立后端心智模型了。
