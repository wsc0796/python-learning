"""
14 — 高级 OOP 练习（抽象类 + 多重继承 + Mixin）
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from abc import ABC, abstractmethod


# ============================================================
# 练习1：抽象类 — 形状
# ============================================================
# 定义一个抽象类 Shape，有抽象方法 area() 和 perimeter()
# 然后实现 Circle 和 Rectangle

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """面积"""
        pass
    

    @abstractmethod
    def perimeter(self) -> float:
        """周长"""
        pass

# TODO: 实现 Circle，接收 radius
class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius

     def area(self):
         result= self.area =3.14*self.radius**2
         return result

     def perimeter(self):
         self.perimeter = 2*3.14*self.radius
         return self.perimeter


# TODO: 实现 Rectangle，接收 width, height
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        result=self.area=self.width*self.height
        return result

    def perimeter(self):
        self.perimeter=2*(self.width+self.height)
        return self.perimeter
# 验证
c = Circle(5)
print(f"圆: 面积={c.area():.2f}, 周长={c.perimeter():.2f}")
r = Rectangle(3, 4)
print(f"矩形: 面积={r.area():.2f}, 周长={r.perimeter():.2f}")

# 取消注释下面这行看看报什么错
# s = Shape()   # ❌ 抽象类不能实例化


# ============================================================
# 练习2：Mixin — 添加序列化功能
# ============================================================

class JSONMixin:
    """混入 JSON 序列化"""
    def to_json(self):
        import json
        return json.dumps(self.__dict__, ensure_ascii=False)

class Student(JSONMixin):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# TODO: 创建一个 Student 类，继承 JSONMixin
# 属性：name, age, score
# 要求能用 .to_json() 输出 JSON
# class Student(JSONMixin):
#     ...

# 验证
s = Student("张三", 20, 92)
print(s.to_json())   # {"name": "张三", "age": 20, "score": 92}


# ============================================================
# 练习3：多重继承 — 飞禽/游禽/鸭子
# ============================================================

class Flyer:
    def move(self):
        return "飞行中"

class Swimmer:
    def move(self):
        return "游泳中"

# TODO: 创建 Duck 继承 Flyer 和 Swimmer
# 猜一下：d.move() 返回什么？
# 然后打印 D.__mro__ 看方法解析顺序
class Duck(Flyer, Swimmer):
     pass

d = Duck()
print(d.move())      # ?
print(Duck.__mro__)  # ?


# ============================================================
# 练习4：Mixin 组合 — 对比问题
# ============================================================

class Device:
    """设备基类"""
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"设备: {self.name}"

class TimestampMixin:
    """混入时间戳"""
    def created_info(self):
        return f"{self.name} 创建于 2026-05-10"

class PowerMixin:
    """混入电源管理"""
    def battery_info(self):
        return f"{self.name} 电量: 80%"

class Phone(Device ,TimestampMixin , PowerMixin):
    def __init__(self,name):
        super().__init__(name)
   
# TODO: 创建一个 Phone 类，继承 Device + TimestampMixin + PowerMixin
# 调用所有方法验证
# class Phone(Device, TimestampMixin, PowerMixin):
#     pass

# 验证
p = Phone("iPhone 17")
print(p.info())
print(p.created_info())
print(p.battery_info())


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 高级 OOP 练习完成！")
