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

### 什么是依赖注入

```python
# ❌ 硬编码依赖
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()   # 写死了，没法换

# ✅ 依赖注入
class UserService:
    def __init__(self, db: Database):  # 从外部传入
        self.db = db
```

### 为什么用 DI

1. **可替换**：测试时换成 MockDatabase，不用连真实数据库
2. **解耦**：UserService 不知道 DB 的具体实现
3. **测试友好**：单元测试不用配数据库

### FastAPI 里的 DI（预告）

```python
from fastapi import Depends

def get_db():
    db = Database()
    yield db
    db.close()  # 请求结束后自动关闭

@app.get("/users")
def get_users(db: Database = Depends(get_db)):
    return db.query_all()
```

---

## 对照 Java

| Java | Python |
|------|--------|
| `Interface` | `Protocol` |
| `@Autowired` | `Depends()` |
| `@Component` | 普通函数 + `yield` |
| `Callable<X, R>` | `Callable[[X], R]` |
| `Optional<String>` | `Optional[str]` 或 `str \| None` |
