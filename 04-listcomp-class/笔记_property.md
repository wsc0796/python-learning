# @property 完整笔记

> 把方法伪装成属性，调用不用加括号 —— 后端必备

---

## 一、本质：解决"不一致"

```python
# 没有 @property
order.price       # 属性，不加括号
order.total()     # 方法，必须加括号——不一致！

# 有 @property
order.price       # 属性
order.total       # 也是属性风格——一致了！
```

`@property` 让**算出来的值**（total/area/age）用起来像**存着的值**一样自然。

---

## 二、三种用法

### 1. 只读（最常见的用法）

```python
class Order:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    @property
    def total(self):           # 只有 getter，没有 setter
        return self.price * self.count

order = Order(10, 3)
print(order.total)  # 30，不加括号
# order.total = 40  # AttributeError: can't set attribute
```

**适用场景：** 面积、总价、年龄（从出生日期算）、状态描述。

### 2. 读写 + 校验（setter）

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # 注意：直接操作 _celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("低于绝对零度！")
        self._celsius = value

t = Temperature(25)
t.celsius = 30       # 走 setter，合法
t.celsius = -300     # 走 setter，报错！
```

**核心：** `_celsius` 是真实存数据的私有属性，`celsius` 是对外暴露的接口（读走 getter、写走 setter）。

### 3. 删除（deleter，很少用）

```python
@celsius.deleter
def celsius(self):
    print(f"删除 {self._celsius}")
    del self._celsius
```

---

## 三、后端实战：数据校验

```python
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age          # 走 setter
        self.email = email      # 走 setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 150):
            raise ValueError(f"年龄不合法: {value}")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"邮箱格式不对: {value}")
        self._email = value
```

**对比 Java：** Java 用 `setAge(int age)` 方法+校验，Python 用 `@age.setter`——做的事一样。

---

## 四、后端实战：权限控制

```python
class Document:
    def __init__(self, content, owner):
        self._content = content
        self.owner = owner
        self._is_admin = False

    @property
    def content(self):
        """读内容——所有人可读"""
        return self._content

    @content.setter
    def content(self, value):
        """修改内容——只有 owner 可以"""
        # 实际项目中从 request/user 对象获取当前用户
        if not self._is_admin:
            raise PermissionError("只有管理员才能修改文档！")
        self._content = value
```

---

## 五、后端实战：计算字段

```python
class Student:
    def __init__(self, name, scores: list):
        self.name = name
        self._scores = scores

    @property
    def scores(self):
        """返回成绩列表的副本，防止外部修改"""
        return self._scores.copy()

    @scores.setter
    def scores(self, values):
        if any(not (0 <= v <= 100) for v in values):
            raise ValueError("成绩必须在 0-100 之间")
        self._scores = values

    @property
    def average(self):
        """平均分——算出来的，只读"""
        return sum(self._scores) / len(self._scores)

    @property
    def max_score(self):
        """最高分——算出来的，只读"""
        return max(self._scores)

s = Student("张三", [92, 88, 75])
print(s.average)     # 85.0，不加括号
print(s.max_score)   # 92，不加括号
```

---

## 六、`@property` vs `@dataclass` 选哪个

| 场景 | 用哪个 |
|------|--------|
| 纯存数据，无校验、无计算 | `@dataclass` |
| 需要 getter/setter 校验 | `@property` |
| 后端 API 校验/转 JSON | `pydantic.BaseModel` |
| 既有 dataclass 又需要校验 | `@dataclass` + `@property` 混用 |

---

## 七、最容易迷糊的点

```
self.celsius    ← 这是 @property 的 getter/setter（对外接口）
self._celsius   ← 这是真实存数据的属性（私有约定）

@celsius.setter  # 这个方法会让 self.celsius = 值 走这里
def celsius(self, value):
    self._celsius = value  # 实际存到 _celsius
```

**在 `__init__` 里：**
- 写 `self.celsius = value` → **会走 setter**（有校验）
- 写 `self._celsius = value` → **绕过 setter**（直接存）

一般而言 `__init__` 里直接操作 `_celsius` 避开设定的校验逻辑，setter 留给后续修改时校验。

## 备考相关

- [[EXAM_PREP/day04/00_今日任务]] — Day 4 面向对象（@property）
