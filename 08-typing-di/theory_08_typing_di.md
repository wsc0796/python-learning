---
aliases:
  - 08-typing-di
---
# 08 — 类型提示进阶 + 依赖注入

> 相关笔记：[模块与类型提示](../05-module-types/theory_05_module_types.md) · [Pydantic 数据校验](../07-pydantic/theory_07_pydantic.md)

## 第一天：类型提示（05-module-types 已学，快速回顾）

```python
def add(a: int, b: int) -> list[int]:
    return [a + b]
```

### 回顾：基础类型注解

```python
name: str = "张三"
count: int = 42
items: list[int] = [1, 2, 3]
```

### 补：联合类型 Union 和 `| None`

有时候一个字段可能有两种类型：

```python
# Python 3.10+: 用 | 连接多个类型
maybe: str | None = None       # 可以是字符串或空
value: int | str = 42          # 可以是整数或字符串

# Python 3.9 及以下：从 typing 导入 Union
from typing import Union, Optional
maybe: Optional[str] = None    # Optional[str] = str | None
value: Union[int, str] = 42    # Union[int, str] = int | str
```

**为什么更新接口的字段要标 `| None`？**

```python
class NoteUpdate(BaseModel):
    content: str | None = Field(default=None, min_length=1)
```

- `str | None` = 这个字段可以是字符串，也可以是空
- `= None` = 默认值是 None（用户不传就不改）
- `min_length=1` = 如果传了，至少 1 个字符

**对比创建接口：**

```python
class NoteCreate(BaseModel):
    content: str = Field(min_length=1)     # 必填
class NoteUpdate(BaseModel):
    content: str | None = Field(default=None, min_length=1)  # 可选
```

创建是"你必须给我内容"，更新是"你想改就改，不改拉倒"。

> **`变量: 类型` 的写法统一读作："这个变量的类型是……"**

**今天只补两个新东西：** `Callable`、`Protocol`，然后进入依赖注入。

---

## 一、Callable：函数作为参数

```python
from typing import Callable

# Callable[[参数类型], 返回值类型]
def process(nums: list[int], transformer: Callable[[int], str]) -> list[str]:
    return [transformer(n) for n in nums]

result = process([1, 2, 3], lambda x: f"第{x}名")
# ['第1名', '第2名', '第3名']
```

## 二、Protocol：鸭子类型

Java 用 interface 定义行为，Python 用 Protocol：

```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, user: str, message: str) -> None: ...

class EmailNotifier:
    def send(self, user: str, message: str):
        print(f"[Email] {user}: {message}")

class SMSNotifier:
    def send(self, user: str, message: str):
        print(f"[SMS] {user}: {message}")
```

```python
class AlertService:
    def __init__(self, notifier: Notifier):  # 只要实现了 send 就行
        self.notifier = notifier

    def alert(self, user: str, message: str):
        self.notifier.send(user, message)

# 使用：传入任何实现了 send 的对象
AlertService(EmailNotifier()).alert("张三", "你好")
AlertService(SMSNotifier()).alert("李四", "验证码: 1234")
```

**不需要继承，不需要 `implements`** —— 只要结构匹配就算实现。

---

## 三、依赖注入（DI）

### 1. 先理解“依赖”是什么

假设有两个类：

```python
class MySQLDatabase:
    def query_all(self) -> list[str]:
        return ["张三", "李四"]

class UserService:
    def get_users(self) -> list[str]:
        ...
```

`UserService` 要查询用户，就必须用到数据库对象。

所以我们说：

```text
UserService 依赖 MySQLDatabase
```

简单记：

```text
A 类里面需要用到 B 类
就说 A 依赖 B
```

### 2. 硬编码依赖：能跑，但绑死了

```python
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()

    def get_users(self) -> list[str]:
        return self.db.query_all()
```

这段代码的问题在这里：

```python
self.db = MySQLDatabase()
```

`UserService` 自己创建了 `MySQLDatabase`，这叫硬编码依赖。

坏处：

1. **不好替换**：以后想换成 SQLite，要改 `UserService`
2. **不好测试**：测试时很难换成假的数据库
3. **职责混乱**：UserService 既处理用户业务，又决定用哪个数据库

### 3. 依赖注入：自己不造，外面传进来

依赖注入就是：

```text
UserService 不自己创建 db
而是让外部把 db 传进来
```

```python
class UserService:
    def __init__(self, db):
        self.db = db

    def get_users(self) -> list[str]:
        return self.db.query_all()

service = UserService(MySQLDatabase())
```

现在 `UserService` 不关心你给它什么数据库。

```python
mysql_service = UserService(MySQLDatabase())
sqlite_service = UserService(SQLiteDatabase())
fake_service = UserService(FakeDatabase())
```

同一个 `UserService`，可以配不同实现。

### 4. 加上 Protocol：像 Java interface 一样规定能力

```python
from typing import Protocol

class Database(Protocol):
    def query_all(self) -> list[str]:
        ...
```

这句话意思是：

```text
只要一个对象有 query_all() 方法
它就可以被当成 Database 使用
```

完整示例：

```python
from typing import Protocol

class Database(Protocol):
    def query_all(self) -> list[str]:
        ...

class MySQLDatabase:
    def query_all(self) -> list[str]:
        return ["张三", "李四"]

class FakeDatabase:
    def query_all(self) -> list[str]:
        return ["测试用户"]

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def get_users(self) -> list[str]:
        return self.db.query_all()

service = UserService(MySQLDatabase())
test_service = UserService(FakeDatabase())
```

重点：

```text
UserService 依赖的不是 MySQLDatabase
而是 Database 这个“能力约定”
```

### 5. 为什么用 DI

1. **可替换**：测试时换成 MockDatabase，不用连真实数据库
2. **解耦**：UserService 不知道 DB 的具体实现
3. **测试友好**：单元测试不用配数据库

更直白地说：

```text
硬编码依赖：我要什么，我自己造
依赖注入：我要什么，外面传给我
```

### 6. 和你现在的 notes-api 对应

你现在写的：

```python
class NoteService:
    def __init__(self, repository: NoteRepository):
        self.repository = repository
```

就是依赖注入。

意思是：

```text
NoteService 不自己创建 JsonNoteRepository
而是外面传进来一个 repository
```

外面可能这样组装：

```python
repo = JsonNoteRepository("notes.json")
service = NoteService(repo)
```

好处是：

```text
现在可以传 JsonNoteRepository
以后也可以传 SqlNoteRepository
测试时可以传 FakeNoteRepository
NoteService 不用改
```

### 7. FastAPI 里的 DI（预告）

普通 Python 里，依赖注入是手动传：

```python
service = NoteService(repo)
```

FastAPI 里，可以让框架帮你传：

```python
from fastapi import Depends

def get_note_service():
    return note_service

@app.get("/notes")
def list_notes(service: NoteService = Depends(get_note_service)):
    return service.list_notes()
```

执行顺序是：

```text
浏览器请求 /notes
  ↓
FastAPI 找到 list_notes()
  ↓
发现 service 参数有 Depends(get_note_service)
  ↓
先执行 get_note_service()
  ↓
拿到 NoteService 对象
  ↓
把它传给 list_notes(service)
  ↓
接口函数正式执行
```

也就是说：

```text
Depends 发生在接口函数执行前
它负责帮你准备依赖对象
```

### 8. 带 yield 的依赖：适合数据库连接

以后连接数据库时常见：

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

意思是：

```text
请求开始前：创建 db
接口执行中：把 db 交给接口使用
请求结束后：关闭 db
```

这就是 FastAPI 依赖注入常用来管理资源生命周期的原因。

### 9. 最重要的一句话

```text
依赖注入 = 自己不造依赖，别人造好传给我
```

在后端项目里就是：

```text
Controller 不自己造 Service
Service 不自己造 Repository
Repository 不自己造一堆业务对象
```

每一层只做自己的事。

---

## 对照 Java

| Java | Python |
|------|--------|
| `Interface` | `Protocol` |
| `@Autowired` | `Depends()` |
| `@Component` | 普通函数 + `yield` |
| `Callable<X, R>` | `Callable[[X], R]` |
| `Optional<String>` | `Optional[str]` 或 `str \| None` |
