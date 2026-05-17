"""
04b — 类/封装/继承/多态 练习（补 Day 2）
theory 在 theory_04_listcomp_lambda_class.md 里
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ============================================================
# 练习1：定义类 + __init__ + self
# ============================================================
# TODO: 定义一个 Student 类
# __init__ 接收 name (str), score (float)
# 有方法 introduce(self) -> str，返回 "我叫xxx，得分xxx"

class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def info(self):
        return f"我叫{self.name},得分{self.score}"

s = Student("张三", 92.5)
print(s.info())   # 我叫张三，得分92.5
# 验证
# s = Student("张三", 92.5)
# print(s.introduce())   # 我叫张三，得分92.5


# ============================================================
# 练习2：封装 — _ 和 __ 的区别
# ============================================================
# TODO: 定义一个 BankAccount 类
# 公开属性：holder (str)
# 保护属性：_balance (float)，默认 0
# 私有属性：__password (str)
# 方法：deposit(amount) → 增加余额
# 方法：get_balance() → 返回余额

class BankAccount:
    def __init__(self, holder: str, password: str,balance: float):
        self.holder = holder
        self._balance = 0.0      # 保护
        self.__password = password  # 私有

    def deposit(self, amount: float):
        # 你的代码...
        if amount >0:
            self._balance += amount

    def get_balance(self) :
        # 你的代码...
        if self._balance>=0:
            return self._balance



acct = BankAccount("张三", "123456","0")
acct.deposit(1)
print(f"{acct.holder} 余额: {acct.get_balance()}")   # 张三 余额: 1000

# 破坏实验（取消注释看报错）：
#print(acct.__password)    # AttributeError!
#print(acct._BankAccount__password)  # 能访问但不建议


# ============================================================
# 练习3：继承
# ============================================================
# TODO: 定义 Animal → Dog, Cat
# Animal: __init__(name), speak() 返回 "..."
# Dog 继承 Animal，speak() 返回 "汪汪"
# Cat 继承 Animal，speak() 返回 "喵喵"

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) :
        return "..."

class Dog(Animal):
    # 你的代码...
    def speak(self):
        return"汪汪"


class Cat(Animal):
    # 你的代码...
    def speak(self):
        return "喵喵"

# 验证
d = Dog("旺财")
c = Cat("咪咪")
print(f"{d.name}: {d.speak()}")   # 旺财: 汪汪
print(f"{c.name}: {c.speak()}")   # 咪咪: 喵喵


# ============================================================
# 练习4：多态（鸭子类型）
# ============================================================
# TODO: 不用继承，定义两个类 Bird 和 Plane
# 都有 fly() 方法，返回字符串
# 然后写一个函数 start_flying(thing) 调用 thing.fly()

class Bird:
   def fly(self):
       return "鸟在飞"

class Plane:
    # 你的代码...
    def fly(self):
        return "飞机在飞"

def start_flying(thing):
    return thing.fly()


print(start_flying(Bird()))    # 鸟在飞
print(start_flying(Plane()))   # 飞机在飞


# ============================================================
# 练习5：super() 调用父类
# ============================================================
# TODO: Employee 继承 Person
# Person: __init__(name, age)
# Employee: __init__(name, age, salary)，用 super() 调父类

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name: str, age: int, salary: float):
        # 你的代码... 用 super().__init__(name, age)
        super().__init__(name, age)

        self.salary = salary

    def info(self) -> str:
        return f"{self.name}, {self.age}岁, 薪资{self.salary}"

# 验证

e = Employee("张三", 25, 15000.0)
print(e.info())   # 张三, 25岁, 薪资15000.0


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 类/OOP 练习完成！")
