# dataclasses：Python 官方版 Lombok

> Java 的 `@Data` → Python 的 `@dataclass`，完全对应
>
> 相关笔记：[[笔记_数据结构统一梳理]] · [[笔记_高阶函数]] · [[笔记_内置函数速查]]

---

## 一、对比：Java Lombok vs Python dataclass

### Java（Lombok）
```java
@Data
public class BankAccount {
    private String owner;
    private double balance;
    private String password;
}
```
自动生成：构造器、getter、setter、toString、equals、hashCode。

### Python（dataclass）
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float
    password: str
```
自动生成：`__init__`、`__repr__`（print 好看）、`__eq__`（比较对象）。

### 手动写的等价代码

```python
# 不用 dataclass 的写法——全是样板代码
class BankAccount:
    def __init__(self, owner, balance, password):
        self.owner = owner
        self.balance = balance
        self.password = password
```
`@dataclass` 自动替你干了上面这些。

---

## 二、常用配置

### 1. 只读（不可变对象，类似 Java final）

```python
@dataclass(frozen=True)
class BankAccount:
    owner: str
    balance: float

# 创建后不能修改
acc = BankAccount("张三", 1000)
acc.balance = 2000  # TypeError: cannot assign to field 'balance'
```

### 2. 默认值

```python
@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0     # 有默认值
    password: str = "123456"
```

### 3. 不参与初始化 / 比较

```python
from dataclasses import dataclass, field

@dataclass
class BankAccount:
    owner: str
    balance: float = field(compare=False)  # 比较时忽略这个字段
    _id: int = field(init=False)           # 不参与初始化，自动生成
```

---

## 三、实战：d ataclass 的银行账户

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0
    account_type: str = "储蓄账户"
    account_id: Optional[str] = None  # 可为空

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

# 使用
acc = BankAccount("张三", 1000)
print(acc)              # 自动好看的输出 ← @dataclass 给的
acc.deposit(500)
print(acc.balance)      # 1500
```

用 `print(acc)` 直接输出 `BankAccount(owner='张三', balance=1500.0, account_type='储蓄账户', account_id=None)`——不需要手写 `__str__`。

---

## 四、Pydantic：比 dataclass 更强的方案（后端 99% 用这个）

> 对应模块：[[07-pydantic]]，pydantic 独立模块有完整 theory + practice

```python
from pydantic import BaseModel

class BankAccount(BaseModel):
    owner: str
    balance: float
    password: str
```

| 功能 | `@dataclass` | `pydantic.BaseModel` |
|------|-------------|---------------------|
| 自动 `__init__` | ✅ | ✅ |
| 自动 `__repr__` | ✅ | ✅ |
| 自动 `__eq__` | ✅ | ✅ |
| 类型校验 | ❌（只是注解） | ✅ 传错类型报错 |
| 自动转 JSON | ❌ | ✅ `.model_dump_json()` |
| 自动转字典 | ❌ | ✅ `.model_dump()` |
| 嵌套校验 | ❌ | ✅ |

```python
# pydantic 自动校验类型
acc = BankAccount(owner="张三", balance="abc", password="123")
# ValidationError: balance 不是合法数字 ← 自动报错
```

---

## 五、你现在在走的路线

| Java | Python | 对应你的模块 |
|------|--------|------------|
| `@Data` / Lombok | `@dataclass` | **04-listcomp-class** |
| Spring Validation | `pydantic.BaseModel` | **07-pydantic** |
| AOP 切面 | 装饰器 | **11-closure-decorator** |
| MyBatis 映射 | SQLAlchemy ORM | 暑假学 |

你现在学的不是"Python 语法"，是**和 Java 完全互通的后端思想**。
