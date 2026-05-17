"""
银行账户综合练习——封装 + @property + 鸭子类型 + 魔法方法

需求：
1. 开户时传入：户名、密码、初始余额
2. 存款：金额 > 0 才存入
3. 取款：需要验证密码 + 余额充足才能取
4. 查询余额：返回当前余额（不判断正负）
5. print(账户) 输出："张三 余额: 1500.0"
6. 两个账户余额相等时视为相等（__eq__）
"""

# ========== TODO 1: 补全类定义 ==========
# 要求：
# - holder 公开
# - _balance 保护
# - __password 私有
class BankAccount:
    def __init__(self, holder: str, password: str, balance: float = 0.0):
        self.holder = holder          # 公开
        self._balance = balance           # TODO: 用传入的 balance
        self.__password = password       # TODO: 用传入的 password

    # ========== TODO 2: 存款 ==========
    # 金额 > 0 才存入，否则打印"存款金额必须大于0"
    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        else:
            print("存款金额必须大于0")

    # ========== TODO 3: 取款（验证密码） ==========
    # 1. 验证密码 -> 不对就打印"密码错误"并 return False
    # 2. 余额够 -> 扣钱，return True
    # 3. 余额不够 -> 打印"余额不足"并 return False
    def withdraw(self,amount:float,password:str):
        if password !=self.__password:
            print("密码错误")
            return False
        if amount > self._balance:
            print("余额不足")
            return False
        self._balance -= amount
        return True
        

    # ========== TODO 4: 查询余额 ==========
    @property
    def balance(self):
        return self._balance


    # ========== TODO 5: __str__ ==========
    # 输出格式: "张三 余额: 1500.0"
    def __str__(self):

        return f"{self.holder} 余额：{self.balance}"

    # ========== TODO 6: __eq__ ==========
    # 两个账户余额相等即视为相等
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False


# ========== 测试代码（不用改） ==========
if __name__ == "__main__":
    acct = BankAccount("张三", "123456", 1000)
    print("--- 存款测试 ---")
    acct.deposit(500)
    print(acct)                    # 张三 余额: 1500.0

    print("--- 取款测试（错误密码）---")
    acct.withdraw(100, "wrong")    # 密码错误
    print(acct)                    # 张三 余额: 1500.0（没扣）

    print("--- 取款测试（正确密码）---")
    acct.withdraw(200, "123456")   # 余额: 1300.0
    print(acct)                    # 张三 余额: 1300.0

    print("--- 取款测试（余额不足）---")
    acct.withdraw(99999, "123456") # 余额不足

    print("--- __eq__ 测试 ---")
    a = BankAccount("李四", "000", 100)
    b = BankAccount("王五", "111", 100)
    print(a == b)  # True（余额都是100）

    print("--- 读取余额 ---")
    print(acct.balance)  # 1300.0（走 @property）
