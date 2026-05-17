"""
11 — 闭包 + 装饰器 练习
为理解 @app.get("/path") 做准备
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from typing import Callable


# ============================================================
# 热身：函数也是变量
# ============================================================
# 在 Python 里，函数可以赋值给变量，可以当参数传

def say_hello(name: str) -> str:
    return f"你好, {name}!"

# TODO: 把 say_hello 赋值给变量 greeter，然后调用它
# greeter = ...
# print(greeter("张三"))   # 你好, 张三!
greeter =say_hello
print(greeter("张三"))

# ============================================================
# 练习1：闭包 — 函数里定义函数
# ============================================================
# 闭包 = 内部函数 + 记住了外部函数的变量

def make_multiplier(n: int) -> Callable:
    """
    接收一个数字 n，返回一个函数。
    返回的函数接收 x，返回 x * n。
    """
    # 你的代码...
    # 在内部定义函数 multiplier(x): return x * n
    # 返回 multiplier
    pass

# 验证
# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5))    # 10
# print(triple(5))    # 15


# ============================================================
# 练习2：闭包常见用途 — 计数器
# ============================================================

def create_counter(start: int = 0) -> Callable:
    """
    返回一个函数，每次调用返回下一个数字。
    create_counter(10)() → 10
    create_counter(10)() → 11
    """
    # 你的代码...
    # 要点：内部函数修改外部变量要用 nonlocal
    pass

# 验证
# counter = create_counter(10)
# print(counter())    # 10
# print(counter())    # 11
# print(counter())    # 12


# ============================================================
# 练习3：写一个简单装饰器
# ============================================================
# 装饰器 = 接收函数，返回包装后的函数

def log_calls(func: Callable) -> Callable:
    """
    装饰器：打印 "调用 {函数名}()" 然后执行原函数。
    """
    # wrapper(*args, **kwargs) 接收任意参数
    # 打印日志
    # 返回 func(*args, **kwargs)
    pass

# 验证
# @log_calls
# def add(a, b):
#     return a + b

# print(add(3, 5))    # 应该先打印日志，再输出 8


# ============================================================
# 练习4：带参数的装饰器 — 模拟 @app.get("/path")
# ============================================================
# 三层结构：最外层接收参数 → 中间层接收函数 → 内层包装

class FakeApp:
    """
    模拟 FastAPI 的 app 对象。
    用法：
        app = FakeApp()
        @app.get("/hello")
        def hello():
            return "Hello!"
        print(app.routes)  # {"/hello": <function hello>}
    """
    def __init__(self):
        self.routes = {}

    def get(self, path: str) -> Callable:
        """
        1. 接收 path
        2. 返回一个装饰器，装饰器把 (path, func) 注册到 self.routes
        3. 返回 func 本身
        """
        # 你的代码...
        pass

# 验证
# app = FakeApp()

# @app.get("/hello")
# def hello():
#     return "Hello!"

# @app.get("/status")
# def status():
#     return {"status": "ok"}

# print("路由表:", app.routes)
# 期望: {'/hello': <function hello>, '/status': <function status>}


# ============================================================
# 练习5：多个装饰器叠加
# ============================================================

def bold(func: Callable) -> Callable:
    """装饰器：让返回值包上 <b> 标签"""
    # 你的代码...
    pass

def italic(func: Callable) -> Callable:
    """装饰器：让返回值包上 <i> 标签"""
    # 你的代码...
    pass

# @bold
# @italic
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("World"))
# 先 italic 再 bold：<b><i>Hello, World!</i></b>


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 闭包+装饰器 练习完成！")
