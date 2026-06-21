# f-string vs `__str__`

> **f-string = 拼字符串的工具**
> **`__str__` = 控制 `print(对象)` 显示什么**
>
> 两个完全不同，但经常配合使用

---

## 一、f-string 是什么

f-string 是 Python 3.6+ 的字符串语法糖，用来快速拼接变量和表达式。

```python
name = "张三"
age = 20
s = f"我叫{name}，今年{age}岁"
# '我叫张三，今年20岁'
```

不需要定义任何东西，直接在任何地方用。对应模块：[[01-fstring]]。

---

## 二、`__str__` 是什么

`__str__` 是**类里面的魔法方法**，作用只有一个：**控制 `print(对象)` 时输出什么。**

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"姓名：{self.name}"  # 这里用了 f-string

p = Person("张三")
print(p)  # 输出：姓名：张三
```

如果没有 `__str__`：
```python
print(p)  # <__main__.Person object at 0x123456> ← 默认输出，没法看
```

---

## 三、它们的关系

```
__str__ 必须 return 一个字符串
              ↓
    你可以用 f-string 来拼这个字符串
```

```python
def __str__(self):
    return f"姓名：{self.name}, 年龄：{self.age}"
#         ↑ f-string        ↑ 类的属性
```

**等价于不用 f-string 的写法：**
```python
def __str__(self):
    return "姓名：" + self.name + ", 年龄：" + str(self.age)
```

f-string 只是让 `__str__` 里的字符串拼接更简洁。

---

## 四、对比

| | f-string | `__str__` |
|--|---------|-----------|
| 是什么 | 字符串语法 | 类的魔法方法 |
| 作用 | 拼接字符串 | 控制 print(对象) 的显示 |
| 在哪里用 | 任何地方 | 只能写在类里面 |
| 需不需要定义 | 不需要，直接用 | 需要在类里定义 |

---

## 五、更多魔法方法

> 详见：[[笔记_dataclass_vs_lombok]] 中的 `__init__` / `__repr__` / `__eq__`

| 魔法方法 | 作用 | 触发时机 |
|---------|------|---------|
| `__init__` | 初始化对象 | 创建对象时 |
| `__str__` | 控制 print 输出 | print(对象) 时 |
| `__repr__` | 控制调试显示 | 交互式环境直接输对象名 |
| `__eq__` | 控制比较行为 | `obj1 == obj2` 时 |
| `__del__` | 对象被销毁时 | 引用计数归零时（非用del时） |

**`__str__` vs `__repr__` 的区别：**
```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"姓名：{self.name}"        # 给人看的

    def __repr__(self):
        return f"Person('{self.name}')"   # 给开发者看的

p = Person("张三")
print(p)       # 姓名：张三       ← __str__
str(p)         # 姓名：张三       ← __str__
repr(p)        # Person('张三')   ← __repr__
```

**`@dataclass` 自动生成 `__str__` 和 `__repr__`**，这也是为什么推荐用 `@dataclass` 而不是手写类。

## 备考相关

- [[EXAM_PREP/day04/00_今日任务]] — Day 4 面向对象（`__str__` / `__repr__`）
