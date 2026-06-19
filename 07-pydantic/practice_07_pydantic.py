"""
07 - Pydantic 练习

核心目标：
1. 用 BaseModel 描述数据结构
2. 用 Field 添加校验约束
3. 用 model_dump()/model_dump_json() 做序列化
4. 理解嵌套模型和模型方法
"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationError


# ============================================================
# 练习1：你的第一个 Pydantic 模型
# ============================================================


class Student(BaseModel):
    id: int
    name: str
    score: float


# ============================================================
# 练习2：加约束
# ============================================================


class Employee(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=18, le=65)
    salary: float = Field(gt=0)
    department: str = "技术部"


# ============================================================
# 练习3：序列化
# ============================================================


class Product(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)


# ============================================================
# 练习4：嵌套模型
# ============================================================


class Address(BaseModel):
    city: str = Field(min_length=1)
    street: str = Field(min_length=1)


class User(BaseModel):
    name: str = Field(min_length=1)
    address: Address


# ============================================================
# 练习5：模型方法
# ============================================================


class Order(BaseModel):
    id: int
    total: float = Field(ge=0)
    status: Literal["pending", "paid", "cancelled"] = "pending"

    def is_paid(self) -> bool:
        return self.status == "paid"

    def apply_discount(self, rate: float) -> None:
        if not 0 <= rate <= 1:
            raise ValueError("折扣 rate 必须在 0 到 1 之间")
        self.total *= 1 - rate


def demo() -> None:
    """运行本文件时展示每个模型的基本用法。"""
    student = Student(id=1, name="张三", score=92.5)
    print(student)
    print(f"name={student.name}, score={student.score}")

    employee = Employee(name="李四", age=25, salary=15000.0)
    print(employee.model_dump())

    product = Product(id=1, name="笔记本电脑", price=5999.0, stock=10)
    print("字典:", product.model_dump())
    print("JSON:", product.model_dump_json())

    user = User(name="王五", address={"city": "南昌", "street": "经开区"})
    print(user)
    print(user.address.city)

    order = Order(id=1, total=100.0, status="paid")
    print(f"已支付: {order.is_paid()}")
    order.apply_discount(0.1)
    print(f"打折后: {order.total}")

    try:
        Employee(name="", age=15, salary=-100)
    except ValidationError as exc:
        print("\n校验失败示例:")
        print(exc)


if __name__ == "__main__":
    demo()
    print("\n07-Pydantic 练习完成！")
