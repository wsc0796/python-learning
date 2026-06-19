"""
08 - 类型提示进阶 + 依赖注入练习

核心目标：
1. 用类型提示让函数签名更清楚
2. 用 Callable 表达“函数作为参数”
3. 用 Protocol 表达“只关心行为，不关心具体类”
4. 用依赖注入把业务类和具体实现解耦
"""

from pathlib import Path
from typing import Callable, Protocol, runtime_checkable


# ============================================================
# 练习0：类型提示快速热身
# ============================================================


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


def first(items: list[int]) -> int | None:
    return items[0] if items else None


# ============================================================
# 练习1：Callable
# ============================================================


def process_names(
    names: list[str],
    transformer: Callable[[str], str],
) -> list[str]:
    return [transformer(name) for name in names]


# ============================================================
# 练习2：Protocol（鸭子类型）
# ============================================================


@runtime_checkable
class Printer(Protocol):
    def print_doc(self, content: str) -> None:
        ...


class ConsolePrinter:
    def print_doc(self, content: str) -> None:
        print(f"[Console] {content}")


class FilePrinter:
    def __init__(self, filename: str | Path | None = None) -> None:
        self.filename = Path(filename) if filename else Path(__file__).with_name("report.txt")

    def print_doc(self, content: str) -> None:
        with self.filename.open("a", encoding="utf-8") as file:
            file.write(f"[File] {content}\n")
        print(f"[File] {content}")


# ============================================================
# 练习3：依赖注入
# ============================================================


class ReportService:
    def __init__(self, printer: Printer) -> None:
        if not isinstance(printer, Printer):
            raise TypeError("printer 必须实现 print_doc(content: str) -> None")
        self.printer = printer

    def report(self, title: str, content: str) -> None:
        formatted = f"=== {title} ===\n{content}"
        self.printer.print_doc(formatted)


# ============================================================
# 练习4：替换实现（理解 DI 好处）
# ============================================================


class UpperCasePrinter:
    def print_doc(self, content: str) -> None:
        print(content.upper())


# ============================================================
# 练习5：用数据库例子理解 DI
# ============================================================


class UserDatabase(Protocol):
    def query_all(self) -> list[str]:
        ...


class MySQLUserDatabase:
    def query_all(self) -> list[str]:
        return ["张三", "李四"]


class FakeUserDatabase:
    def query_all(self) -> list[str]:
        return ["测试用户"]


class UserService:
    def __init__(self, db: UserDatabase) -> None:
        self.db = db

    def get_users(self) -> list[str]:
        return self.db.query_all()


def demo() -> None:
    print(add(3, 5))
    print(greet("Python"))
    print(first([1, 2, 3]))
    print(first([]))

    shout = lambda text: text.upper() + "!"
    print(process_names(["hello", "world"], shout))

    ConsolePrinter().print_doc("Hello Console")
    FilePrinter().print_doc("Hello File")

    service = ReportService(ConsolePrinter())
    service.report("日报", "今天学习了 Pydantic 和 DI")

    service2 = ReportService(UpperCasePrinter())
    service2.report("通知", "hello world")

    try:
        ReportService("not_a_printer")
    except TypeError as exc:
        print(f"错误示例: {exc}")

    mysql_user_service = UserService(MySQLUserDatabase())
    fake_user_service = UserService(FakeUserDatabase())
    print("真实数据库:", mysql_user_service.get_users())
    print("测试数据库:", fake_user_service.get_users())


if __name__ == "__main__":
    demo()
    print("\n08-类型提示+DI 练习完成！")
