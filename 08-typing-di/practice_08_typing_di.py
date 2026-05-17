"""
08 — 类型提示进阶 + 依赖注入练习
先快速回顾类型提示，再进入 DI。
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from typing import Callable, Protocol, Optional

# ============================================================
# 练习0：类型提示快速热身（来自 05-module-types）
# ============================================================
# 给下面的函数加上类型提示，不用写逻辑

def add(a, b):     # TODO: 加类型提示，int → int
    return a + b

def greet(name):   # TODO: str → str
    return f"Hello, {name}!"

def first(items):  # TODO: list[int] → Optional[int]
    return items[0] if items else None

# 验证
# print(add(3, 5))
# print(greet("Python"))
# print(first([1, 2, 3]))
# print(first([]))


# ============================================================
# 练习1：Callable
# ============================================================
# TODO: 补全类型提示，processor 是一个函数，接收 str 返回 str

def process_names(names: list[str], transformer: Callable[[str], str]) -> list[str]:
    # 你的代码... 列表推导式
    pass

# 验证
# shout = lambda s: s.upper() + "!"
# print(process_names(["hello", "world"], shout))   # ['HELLO!', 'WORLD!']


# ============================================================
# 练习2：Protocol（鸭子类型）
# ============================================================
# TODO: 定义一个 Printer Protocol
# 要求有 print_doc(self, content: str) -> None 方法
# 然后实现两个类：ConsolePrinter 和 FilePrinter

class Printer(Protocol):
    # 你的代码...
    pass

class ConsolePrinter:
    # 打印到控制台
    pass

class FilePrinter:
    # 打印到文件（用 with open）
    pass

# 验证
# cp = ConsolePrinter()
# cp.print_doc("Hello Console")     # 期望: [Console] Hello Console
# fp = FilePrinter()
# fp.print_doc("Hello File")        # 期望: [File] Hello File（且保存到文件）


# ============================================================
# 练习3：依赖注入
# ============================================================
# TODO: 实现 ReportService
# 它接收一个 Printer，调用 printer 来输出报告
# report() 方法接收 title 和 content，输出格式化的报告

class ReportService:
    # 你的代码...
    pass

# 验证
# service = ReportService(ConsolePrinter())
# service.report("日报", "今天学习了 Pydantic 和 DI")


# ============================================================
# 练习4：替换实现（破坏实验 + 理解 DI 好处）
# ============================================================
# 不用改 ReportService 的代码，替换 Printer 实现
# 下面这个 UpperCasePrinter 把所有内容转大写

class UpperCasePrinter:
    # 你的代码...
    pass

# 验证
# service2 = ReportService(UpperCasePrinter())
# service2.report("通知", "hello world")     # 应该输出大写


# ============================================================
# 练习5（破坏实验）
# ============================================================
# 如果传入的对象没有实现 print_doc 方法，会怎样？
# TODO: 取消注释，看报错

# service3 = ReportService("not_a_printer")
# service3.report("测试", "会不会报错？")


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 08-类型提示+DI 练习完成！")
