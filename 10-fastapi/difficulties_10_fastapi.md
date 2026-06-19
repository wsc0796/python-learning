---
date: 2026-05-19
status: 进行中
---

# 10 — FastAPI 学习难点记录

> 本文件记录了学习 `10-fastapi` 项目时遇到的每一个障碍、当时的误解，以及最终的理解。
> 这些内容不会出现在理论笔记里，但它们是真正阻碍你前进的东西。

---

## 难点 1：`类名 + 括号` 到底是什么意思

**卡住的代码：**

```python
task_repository = JsonTaskRepository(DATA_FILE)
```

**当时的困惑：** 括号里放 DATA_FILE 是什么意思？这个语法从哪里学的？

**最终理解：**

`JsonTaskRepository(DATA_FILE)` 就是造一个对象，括号里是传给 `__init__` 的参数。

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("大黄")   # ← 和 JsonTaskRepository(DATA_FILE) 是同一个语法
my_dog.bark()           # 输出：大黄 在叫
```

Python 里所有 `类名(参数)` 都是造对象，没有例外：
- `Path("tasks.json")` → 造 Path 对象
- `TaskService(task_repository)` → 造 TaskService 对象
- `JsonTaskRepository(DATA_FILE)` → 造 JsonTaskRepository 对象

**关键认知：** class 是模具，`ClassName(args)` 是用模具压一个实物出来。括号 = 初始化信息的传递。

---

## 难点 2：为什么需要 dependencies.py（依赖注入的理解）

**当时的困惑：** 这段话"这里创建真实对象，接口函数通过 Depends(get_task_service) 使用它"看了也就看了，不知道有什么用。

**最终理解：**

| 没有 dependencies.py（直接写死） | 有 dependencies.py |
|---|---|
| 每个路由函数自己 `new` 对象 | 对象创建集中到一处 |
| 换存储要改 N 个文件 | 只改 dependencies.py 一行 |
| 测试时没法替换 | FastAPI 支持 `dependency_overrides` 临时换掉 |

**核心口诀：** "创建对象"和"使用对象"分家。dependencies.py 是唯一的"组装车间"。

**调用链：**
```
FastAPI 收到请求
  → Depends(get_task_service)     ← 调 dependencies 里的函数
    → 返回 task_service            ← dependencies 提前创建好的单例
      → 塞给路由函数参数 service    ← main.py 只管用
```

---

## 难点 3：`Annotated + Depends()` 看不懂

**卡住的代码：**

```python
TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]
```

**当时的困惑：** 这一整段是啥？`Annotated` 是什么？`Depends` 怎么工作的？

**最终理解（逐块拆开）：**

```python
Annotated[ TaskService , Depends(get_task_service) ]
#         ~~~~~~~~~~~   ~~~~~~~~~~~~~~~~~~~~~~~~
#           ① 类型标签             ② 取货指令
#         "这是 TaskService"    "FastAPI 帮我去调 get_task_service() 拿值"
```

**`Depends(函数)` 做的事：** 告诉 FastAPI "这个参数的值不是用户传的，你帮我去执行那个函数，把返回值塞进来。"

```python
# 不用 Depends：你自己调
@app.post("/tasks")
def create_task(task: TaskCreate):
    service = get_task_service()      # 手写
    return service.create_task(task)

# 用 Depends：FastAPI 帮你调
@app.post("/tasks")
def create_task(task: TaskCreate, service: TaskServiceDep):
    return service.create_task(task)  # service 已经在参数里了
```

---

## 难点 4：`model_dump()` 没见过

**卡住的代码：**

```python
payload = {"tasks": [task.model_dump() for task in tasks]}
```

**当时的困惑：** 笔记里只有 `d1 = {"name": "小明"}`、`d2 = dict(name="小明")`，没见过 `.model_dump()`。

**最终理解：**

`model_dump()` 是 Pydantic 对象自带的方法——把对象转成普通字典。

```python
task = TaskRead(id=1, title="测试", priority=5, completed=False)

d = task.model_dump()
# {"id": 1, "title": "测试", "priority": 5, "completed": False}
```

**为什么必须转？** `json.dump()` 不认识 Pydantic 对象，只认识 Python 原生类型（dict/list/str/int）。`model_dump()` 就是那座桥。

**补充到笔记的三种字典创建方式：**
```python
# 方式1：花括号
d1 = {"name": "小明", "age": 18}

# 方式2：dict() 构造
d2 = dict(name="小明", age=18)

# 方式3：空字典
d3 = {}
d4 = dict()

# 方式4：从 Pydantic 对象转换 ← 新增
d5 = obj.model_dump()
```

---

## 难点 5：`model_validate()` 没见过

**代码位置：** `repository.py` 第 38 行

```python
return [TaskRead.model_validate(raw_task) for raw_task in raw_tasks]
```

**理解：** `model_validate()` 是 `model_dump()` 的逆向操作——从字典创建 Pydantic 对象，同时做校验。

```python
raw = {"id": 1, "title": "测试", "priority": 5, "completed": False}

task = TaskRead.model_validate(raw)    # 字典 → 对象（顺便校验字段类型和约束）
```

对照创建对象的三种方式：
```python
# 方式1：直接传参
TaskRead(id=1, title="测试", priority=5)

# 方式2：解包字典
TaskRead(**{"id": 1, "title": "测试", "priority": 5})

# 方式3：model_validate ← 新增
TaskRead.model_validate({"id": 1, "title": "测试", "priority": 5})
```

方式3最安全——数据来源不信任时用它（文件、外部API、用户输入），它会完整校验。

---

## 难点 6：`model_copy()` 创建副本

**代码位置：** `service.py` 第 51 行

```python
completed_task = task.model_copy(update={"completed": True})
```

**理解：** 不修改原对象，创建一个新对象并把指定字段改成新值。

```python
task = TaskRead(id=1, title="测试", priority=5, completed=False)

new_task = task.model_copy(update={"completed": True})
# new_task = TaskRead(id=1, title="测试", priority=5, completed=True)
# task 不变：completed 还是 False
```

等价于手写：
```python
new_task = TaskRead(
    id=task.id,
    title=task.title,
    priority=task.priority,
    completed=True,          # 只有这个改了
)
```

---

## 难点 7：`max(..., default=0)` 空列表兜底

**卡住的代码：**

```python
next_id = max((task.id for task in tasks), default=0) + 1
```

**逐截拆开：**

```python
# ① (task.id for task in tasks)      → 生成器：逐个取出 .id，如 1, 3, 2
# ② max(..., default=0)               → 取最大。列表空时兜底返回 0
# ③ + 1                               → 自增一位
```

```python
# 列表有内容：max → 3，+1 → 4（下一条 id=4）
# 列表为空：  max → 0，+1 → 1（第一条 id=1）
```

---

## 难点 8：Protocol 看不懂

**卡住的代码：**

```python
class TaskRepository(Protocol):
    def list_tasks(self) -> list[TaskRead]: ...
    def save_tasks(self, tasks: list[TaskRead]) -> None: ...
```

**当时的困惑：** 这个 Protocol 存在的作用是什么？

**最终理解：**

Protocol = 行为约定（长得像就行，不需要继承）。`JsonTaskRepository` 没写 `class JsonTaskRepository(TaskRepository)`，但只要它有 `list_tasks` 和 `save_tasks` 方法，就自动满足 `TaskRepository` 协议。

**为什么不用继承？** Python 的 Protocol 是 structural subtyping（Go 的 interface 也这样）——不看你声明了什么，只看你有什么方法。

**核心价值：** service 只依赖 Protocol，不依赖具体实现。想换存储时：
```python
# 原来：JSON 文件存储
task_repository = JsonTaskRepository(DATA_FILE)

# 改成：SQLite 存储（只改这一行！）
task_repository = SqlTaskRepository("tasks.db")
```

---

## 难点 9：Pydantic 校验输入 vs 规范输出的完整流程

**当时的困惑：** 理解不了 Pydantic 如何校验输入数据和规范输出数据。

**最终理解 —— 一次 POST 请求的完整旅程：**

```
用户发送 POST /tasks  {"title": "测试", "priority": 5}
        │
        ▼
FastAPI 路由    task: TaskCreate    ← Pydantic 校验输入（入库关）
        │       - title 至少1字符 ✓
        │       - priority 1-5 ✓
        │       - 多余字段被拒绝
        ▼
Service 层      TaskRead(           ← 加上 id 和 completed（转换关）
                  id=next_id,
                  title=task_create.title,
                  priority=task_create.priority,
                  completed=False
                )
        │
        ▼
Repository 层   task.model_dump()   ← 对象转字典（持久化关）
                json.dump(...)       ← 写入 tasks.json
        │
        ▼
FastAPI 响应    response_model=TaskRead  ← Pydantic 规范输出（出库关）
        │       - 只输出 4 个字段
        │       - id>=1 再校验一遍
        ▼
用户收到       {"id":1, "title":"测试", "priority":5, "completed":false}
```

**两个模型的分工：**

| | TaskCreate | TaskRead |
|---|---|---|
| 用在哪 | 输入（POST 请求体） | 输出（响应体）+ 持久化 |
| 有哪些字段 | title, priority | id, title, priority, completed |
| 谁负责 | "脏数据别进来" | "输出格式统一" |

---

## 难点 10：`save_tasks()` 逐行理解

**当时完全看不懂：**

```python
def save_tasks(self, tasks: list[TaskRead]) -> None:
    self.filename.parent.mkdir(parents=True, exist_ok=True)         # 确保目录存在
    payload = {"tasks": [task.model_dump() for task in tasks]}      # 对象列表 → 字典列表

    with self.filename.open("w", encoding="utf-8") as file:         # 打开文件
        json.dump(payload, file, ensure_ascii=False, indent=2)      # 写入 JSON
```

**逐行翻译：**
1. 确保 `tasks.json` 所在的文件夹存在（没有就创建）
2. 把每个 TaskRead 对象转成字典，包装成 `{"tasks": [...]}`
3. 打开 `tasks.json`，准备覆盖写入
4. 把字典序列化成 JSON 字符串写入，保留中文，缩进 2 格

**为什么 `model_dump()` 必须放在 `json.dump()` 之前？**
因为 `json.dump()` 是 Python 标准库，它不认识 Pydantic 对象，只认识 dict。必须先转。

---

## 难点 11：`bool | None = None` 看不懂

**卡住的代码：**

```python
def list_tasks(self, completed: bool | None = None) -> list[TaskRead]:
```

**当时的困惑：** 这一串是什么？`bool | None` 是什么意思？

**逐块拆开：**

```python
completed: bool | None = None
#         ~~~~~~~~~~~~   ~~~~
#           类型标注      默认值
#      "可以是 True/False/None"    "不传就是 None"
```

- `bool | None` = Union 类型，这个参数可以传 `True`、`False`、`None` 三种值之一
- `= None` = 默认值是 `None`（调用时不传这个参数，就用 `None`）
- `None` 在这里充当"哨兵值"（sentinel）——代表"用户没有指定筛选条件"

**为什么三个值都要？** 因为 `True` 和 `False` 已经有语义了（筛选已完成/未完成），所以需要一个第三值来表达"不过滤"。这个第三值就是 `None`。

---

## 难点 12：`if completed is None` 的逻辑

**卡住的代码：**

```python
if completed is None:
    return tasks                          # 全返回
return [task for task in tasks if task.completed == completed]   # 过滤
```

**当时的困惑：** `task.completed == completed` —— 两个 `completed` 分不清。

**拆开：**

```python
# ⚠️ 注意！这两个 completed 是不同的东西
for task in tasks:
    if task.completed == completed
#      ~~~~~~~~~~~~~   ~~~~~~~~~
#      任务的字段值      参数的值
#      (每个任务自己的)  (调用者传进来的 True/False/None)
```

用人话翻译：

| 调用方式 | `completed` 参数值 | 行为 |
|---------|-------------------|------|
| `service.list_tasks()` | `None` | 第一个 if 命中 → 返回全部 |
| `service.list_tasks(completed=True)` | `True` | 第一个 if 不命中 → 只返回 `task.completed == True` 的任务 |
| `service.list_tasks(completed=False)` | `False` | 第一个 if 不命中 → 只返回 `task.completed == False` 的任务 |

---

## 难点 13：`json.load()` vs `json.dump()` 方向记反

**卡住的代码：**

```python
with self.filename.open("r") as file:
    payload = json.load(file)    # ← 把文件内容读成 Python 字典
```

**当时的误解：** 以为这是"序列化"。

**纠正口诀：**

```
dump  → 倒出去（序列化）：Python 对象 → JSON 字符串 → 写入文件
load  → 装进来（反序列化）：文件里的 JSON 字符串 → Python 对象

对称操作：
    save_tasks: 对象 ──model_dump()──→ 字典 ──json.dump()──→ 文件
    list_tasks:  文件 ──json.load()──→ 字典 ──model_validate()──→ 对象
```

---

## 难点 14：不知道代码怎么从零开始写

**当时的困惑：** 知道要写什么功能（比如"保存笔记"），但不知道如何从需求变成代码。感觉代码是凭空蹦出来的。

**核心方法：需求 → 翻译成人话步骤 → 每步对应一行代码。**

以 `save_notes` 为例：

```
需求：我要保存 notes

翻译成步骤：
  1. 文件夹要存在          → self.filename.parent.mkdir(parents=True, exist_ok=True)
  2. 对象不能直接写 JSON   → 要转 dict（用 model_dump()）
  3. 多个对象要循环转       → [note.model_dump() for note in notes]
  4. 包成 {"notes": [...]}  → payload = {"notes": [循环结果]}
  5. 打开文件              → with self.filename.open("w", ...) as file:
  6. json.dump 写进去       → json.dump(payload, file, ...)
```

**核心原则：先想人话步骤，再找对应的代码。** 每一步都对应一个你已知的语法或库函数。如果你发现某一步对不上，说明那一步你还没掌握——那个才是真正该查的东西。

**对照 Task 项目写 Note 项目的方法：**

```
1. 左边打开 Task 项目的文件（只读）
2. 右边打开 Note 项目的空文件
3. 看左边一行，翻译成 Note 版本，写到右边
4. 逻辑一模一样的照抄（json.load、json.dump、model_validate 一个字母不改）
5. 只改这些：Task→Note, task→note, tasks→notes
```

---

## 本次学习收获的"口诀"

| 口诀 | 含义 |
|------|------|
| 括号 = 造对象 | `ClassName(args)` = 传参数给 `__init__`，造对象 |
| 组装车间 | dependencies.py 只负责创建和连线，不参与业务 |
| 对象转字典 | `model_dump()` = Pydantic → Python dict |
| 字典转对象 | `model_validate()` = Python dict → Pydantic（带校验） |
| 副本改字段 | `model_copy(update={...})` = 不修改原对象，新建一个 |
| 空列表兜底 | `max(seq, default=0)` = 空的时候别报错，用0 |
| Protocol = 拍胸脯 | 只要你有这些方法，我就信任你，不管你怎么实现的 |
| `bool \| None` | Union 类型：参数可以是 True、False、None 三种值之一 |
| `None` 做哨兵值 | 当 True/False 已有语义时，用 None 代表"未指定" |
| dump=倒，load=装 | dump 写出去（序列化），load 读进来（反序列化）|
| 参数名 vs 字段名 | `task.completed == completed`：前面是字段值，后面是参数值 |
| 需求→步骤→代码 | 不要直接写代码，先把需求翻译成人话步骤，每步再找对应语法 |
| 照着抄，只改名字 | 左边开原文件，右边写新文件，逻辑照抄，只改 Task→Note |
