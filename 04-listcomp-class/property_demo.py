"""
@property 从零演示
运行：python property_demo.py
一步一步看，别跳
"""

print("=" * 50)
print("第1步：没有 @property 的普通类")
print("=" * 50)

class Order1:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total(self):  # 普通方法
        return self.price * self.count

o1 = Order1(10, 3)
print(f"  price: {o1.price}")    # 属性，不加括号
print(f"  count: {o1.count}")    # 属性，不加括号
print(f"  total: {o1.total()}")  # 方法，必须加括号——不一致！

input("\n按回车看第2步...")


print("=" * 50)
print("第2步：加上 @property 之后")
print("=" * 50)

class Order2:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    @property
    def total(self):  # 加了 @property，方法变成"属性风格"
        return self.price * self.count

o2 = Order2(10, 3)
print(f"  price: {o2.price}")   # 不加括号
print(f"  count: {o2.count}")   # 不加括号
print(f"  total: {o2.total}")   # 也不加括号——一致了！

input("\n按回车看第3步...")


print("=" * 50)
print("第3步：为什么要用 @property——从"存的值"变成"算的值"")
print("=" * 50)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """面积是算出来的，不是存的"""
        return self.width * self.height

    @property
    def perimeter(self):
        """周长也是算出来的"""
        return 2 * (self.width + self.height)

r = Rectangle(5, 3)
print(f"  width: {r.width}")
print(f"  height: {r.height}")
print(f"  area: {r.area}")       # 像读属性一样
print(f"  perimeter: {r.perimeter}")  # 像读属性一样

# 如果 width 变了，area 自动跟着变
print("\n  把 width 改成 10...")
r.width = 10
print(f"  area 自动变成: {r.area}")  # 不用重新调用

input("\n按回车看第4步...")


print("=" * 50)
print("第4步：setter——控制"赋值"的时候做什么")
print("=" * 50)
print("  上面那些 @property 都是"只读"的")
print("  如果也想控制"赋值"，需要加 setter")

class Temperature:
    def __init__(self, celsius):
        # 注意：这里直接操作 _celsius，不走 setter
        self._celsius = celsius

    @property
    def celsius(self):
        """读温度"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """写温度——可以加校验"""
        print(f"  → setter 被调用了，赋值: {value}")
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度！")
        self._celsius = value

t = Temperature(25)
print(f"  读温度: {t.celsius}")      # 走 @property，不加括号

t.celsius = 30                        # 走 setter
print(f"  改后: {t.celsius}")

# 试试非法值
print("\n  尝试设置 -300 度...")
try:
    t.celsius = -300
except ValueError as e:
    print(f"  捕获错误: {e}")

print("\n")
print("=" * 50)
print("总结")
print("=" * 50)
print("""
@property = 方法伪装成属性，调用不用加括号

不需要 setter 的场景：
  那些"算出来的值"——比如 total、area、perimeter
  只用 @property 就够了，不用 setter

需要 setter 的场景：
  你希望在"赋值"的时候做点别的事（校验、转换、记录日志）
  就用 @property + @xxx.setter

一句话：
  @property 解决"读"的问题
  @xxx.setter 解决"写"的问题
  不需要"写"就别写 setter
""")
