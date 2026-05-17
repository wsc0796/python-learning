"""
07 — Pydantic 练习
做完再去动 Day 5 的 CRUD。
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from pydantic import BaseModel, Field

# ============================================================
# 练习1：你的第一个 Pydantic 模型
# ============================================================
# TODO: 定义一个 Student 模型
# 字段：id (int), name (str), score (float)

class Student(BaseModel):
    # 你的代码...
    pass

# 验证 - 取消注释跑通
# s = Student(id=1, name="张三", score=92.5)
# print(s)
# print(f"name={s.name}, score={s.score}")


# ============================================================
# 练习2：加约束
# ============================================================
# TODO: 定义一个 Employee 模型
# name: 至少1字符
# age: 18-65
# salary: 大于0
# department: 可选，默认"技术部"

class Employee(BaseModel):
    # 你的代码...
    pass

# 验证 - 取消注释跑通
# e = Employee(name="张三", age=25, salary=15000.0)
# print(e.model_dump())

# 下面的应该报错，取消注释看报错
# e2 = Employee(name="", age=15, salary=-100)   # 三个都违反约束


# ============================================================
# 练习3：序列化
# ============================================================
# TODO: 创建一个 Product 模型
# 字段：id, name, price, stock（默认0）
# 然后：创建实例 → model_dump() → model_dump_json()

class Product(BaseModel):
    # 你的代码...
    pass

# 验证 - 取消注释跑通
# p = Product(id=1, name="笔记本电脑", price=5999.0, stock=10)
# print("字典:", p.model_dump())
# print("JSON:", p.model_dump_json())


# ============================================================
# 练习4：嵌套模型（破坏实验）
# ============================================================

class Address(BaseModel):
    city: str
    street: str

class User(BaseModel):
    name: str
    address: Address

# TODO: 取消注释，观察输出
# u = User(name="张三", address={"city": "南昌", "street": "经开区"})
# print(u)
# print(u.address.city)   # 访问嵌套字段

# TODO: 故意传错 → u2 = User(name="张三", address="not_a_dict")
# 取消注释看报错


# ============================================================
# 练习5：模型方法
# ============================================================
# TODO: 在模型上加一个自定义方法
# 模型：Order，字段 id, total (float), status (str)
# 方法：is_paid() → bool (status == "paid")
# 方法：apply_discount(rate: float) → 修改 total

class Order(BaseModel):
    id: int
    total: float
    status: str = "pending"

    def is_paid(self) -> bool:
        # 你的代码...
        pass

    def apply_discount(self, rate: float):
        # 你的代码... total *= (1 - rate)
        pass

# 验证
# o = Order(id=1, total=100.0, status="paid")
# print(f"已支付: {o.is_paid()}")
# o.apply_discount(0.1)
# print(f"打折后: {o.total}")    # 90.0


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 07-Pydantic 练习完成！")
