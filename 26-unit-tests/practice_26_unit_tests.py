"""
CS50P 补充 — 单元测试练习

TODO: 完成以下 3 组测试练习
运行方式: pytest practice_26_unit_tests.py -v
"""

# ============================================================
# 练习1: 测试纯函数
# ============================================================

def is_valid_email(email: str) -> bool:
    """判断字符串是否是合法邮箱（简化版）"""
    return "@" in email and "." in email.split("@")[-1]


# TODO: 写 4 个测试用例
#   1. 合法邮箱 (test@example.com)
#   2. 没有@符号 (testexample.com)
#   3. 没有域名 (.com) 部分 (test@)
#   4. 空字符串


# ============================================================
# 练习2: 测试异常
# ============================================================

def safe_divide(a, b):
    """安全除法：除数为0抛出 ValueError"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


# TODO: 写 3 个测试用例
#   1. 正常除法 (10/2 = 5)
#   2. 除数为 0 应抛出 ValueError
#   3. 浮点数除法 (7/2 = 3.5)


# ============================================================
# 练习3: 用 pytest 测试一个有状态的类
# ============================================================

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: str, price: float):
        if price <= 0:
            raise ValueError("价格必须大于0")
        self.items.append({"item": item, "price": price})

    def total(self) -> float:
        return sum(item["price"] for item in self.items)

    def count(self) -> int:
        return len(self.items)


# TODO: 写 4 个测试用例
#   1. 空购物车 total 为 0
#   2. 添加一个商品后 count 为 1
#   3. 添加两个商品后 total 正确
#   4. 添加价格为负的商品应抛出 ValueError


# ============================================================
# 运行: pytest practice_26_unit_tests.py -v
# 看到绿条 = 过，红条 = 有 bug
# ============================================================
