---
aliases:
  - 12-design-patterns
---
# 12 — 设计模式（Python 版）

> 相关笔记：[OOP 深入](../15-oop-deep-dive/theory_15_oop_deep_dive.md) · [闭包与装饰器](../11-closure-decorator/theory_11_closure_decorator.md)

## 说明

你已从 Java 知道设计模式的概念。这里只讲 **Python 特有的实现差异**——大部分模式在 Python 中更简洁，因为函数是一等公民、没有接口强制、有装饰器语法糖。

---

## 1. 单例模式

```python
# Python 最优雅的单例：模块导入一次就是单例
# singleton.py
class Database:
    def query(self):
        return "data"

db = Database()  # 模块级别 = 全局唯一

# 其他文件引入：
# from singleton import db  # 永远是同一个实例
```

```python
# 如果你非要 class 级别的：
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

---

## 2. 工厂模式

```python
# Java 需要 Factory 类 + switch
# Python 直接用字典映射函数

class Dog:
    def speak(self): return "汪汪"

class Cat:
    def speak(self): return "喵喵"

# "工厂"就是个字典
animal_factory = {
    "dog": Dog,
    "cat": Cat,
}

def create_animal(animal_type: str):
    cls = animal_factory.get(animal_type)
    if not cls:
        raise ValueError(f"未知类型: {animal_type}")
    return cls()

a = create_animal("dog")
print(a.speak())  # 汪汪
```

---

## 3. 策略模式

```python
# Java：Strategy 接口 → 多个实现类 → Context 持有引用
# Python：函数就是策略

# 不用接口，不用类，直接传函数
def quick_sort(data):
    return sorted(data)

def reverse_sort(data):
    return sorted(data, reverse=True)

class DataProcessor:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy  # 接收函数

    def process(self, data):
        return self.sort_strategy(data)

p = DataProcessor(reverse_sort)
print(p.process([3, 1, 2]))  # [3, 2, 1]
```

---

## 4. 观察者模式

```python
# Java：Observer 接口 + Observable
# Python：直接用列表存回调函数

class EventEmitter:
    def __init__(self):
        self._listeners = []

    def on(self, callback):
        self._listeners.append(callback)

    def emit(self, data):
        for cb in self._listeners:
            cb(data)

# 使用
def on_login(user):
    print(f"日志: {user} 登录了")

def send_notification(user):
    print(f"通知: 欢迎 {user}")

emitter = EventEmitter()
emitter.on(on_login)          # 注册观察者
emitter.on(send_notification)

emitter.emit("张三")
# 日志: 张三 登录了
# 通知: 欢迎 张三
```

---

## 5. 装饰器模式（Python 内置语法糖）

```python
# Java：BufferedReader br = new BufferedReader(new FileReader("f.txt"))
# Python：@ 语法就是装饰器模式的内置实现

def log_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.time()-start:.2f}s")
        return result
    return wrapper

@log_time
def heavy_task():
    sum(range(1000000))

heavy_task()
```

---

## 对照 Java

| 模式 | Java | Python 差异 |
|------|------|------------|
| Singleton | `private` 构造 + `getInstance()` | 模块级别天然单例 |
| Factory | `interface Product` + 工厂类 | 字典映射函数 |
| Strategy | `interface Strategy` + 实现类 | 直接传函数 |
| Observer | `Observer` 接口 + `Observable` | 函数回调列表 |
| Decorator | `BufferedReader br = new BFR(new FR(f))` | `@decorator` 语法 |
| Template | 抽象类 + 子类实现步骤 | 一样，用 ABC |
