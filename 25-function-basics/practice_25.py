"""
函数基础练习
规则：每个 TODO 手敲代码，不要复制粘贴
"""

# ======== 基础题 ========

# TODO 1: 定义一个无参函数
# 定义函数 say_hello，打印 "Hello, Python!"
# 然后调用它
def say_hello():
    print("hello,python!")
say_hello()
# TODO 2: 定义带参函数
# 定义函数 square(n)，返回 n 的平方
# 调用 square(5)，打印结果
def square(n):
    return n**2
n=square(2)
print(square(2))
print(n)
# TODO 3: 多个参数
# 定义函数 rectangle_area(width, height)，返回矩形面积
# 测试：rectangle_area(5, 3) → 15
def rectangle_area(width,height):
    return width*height
print(rectangle_area(5, 3))

# TODO 4: 默认参数
# 定义函数 power(base, exp=2)，返回 base 的 exp 次方
# 测试：
#   power(3)    → 9（使用默认值）
#   power(3, 3) → 27

def power(base,exp=2):
    return base**exp
print(power(4))
# ======== 综合题 ========

# TODO 5: 返回多个值
# 定义函数 divide(a, b)，返回 (商, 余数) 的元组
# 调用后解包赋值给两个变量并打印

# TODO 6: 函数的组合使用
# 定义函数 is_even(n) — 判断偶数，返回 True/False
# 定义函数 filter_evens(nums) — 用 is_even 过滤列表中的偶数
# 测试：filter_evens([1, 2, 3, 4, 5, 6]) → [2, 4, 6]

# TODO 7: 类型提示 + docstring
# 定义一个函数 celsius_to_fahrenheit(c: float) -> float
# 转换公式：F = C * 9/5 + 32
# 写 docstring 说明参数和返回值的含义
# 测试：celsius_to_fahrenheit(100) → 212.0

# TODO 8: 函数嵌套调用
# 定义三个简单函数：
#   add(a, b) — 返回 a + b
#   multiply(a, b) — 返回 a * b
#   calculate(x, y) — 返回 multiply(add(x, y), add(x, 1))
# 测试 calculate(2, 3) → (2+3) * (2+1) = 15

# ======== 破坏实验 ========

# TODO 9: 定义一个函数，里面有个变量
# 在函数外部访问这个变量，观察报错
def test_scope():
    x = 10  # 这是一个局部变量
    print(f"函数内部的 x: {x}")

# TODO 10: 定义一个函数不写 return
# 把调用结果赋值给一个变量并打印，观察值是什么
def no_return():
    print("这个函数没有 return")
