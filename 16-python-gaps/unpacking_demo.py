"""
unpacking_demo.py — 解包操作实战演示
运行：python unpacking_demo.py
"""

# ============================================================
# 1. 基础解包
# ============================================================
print("=" * 40)
print("1. 基础解包")
print("=" * 40)

# 列表解包
a, b, c = [1, 2, 3]
print(f"列表解包：a={a}, b={b}, c={c}")

# 元组解包（函数返回多个值）
def get_user():
    return "张三", 25, "南昌"

name, age, city = get_user()
print(f"函数返回值解包：name={name}, age={age}, city={city}")

# 字符串解包
x, y, z = "ABC"
print(f"字符串解包：x={x}, y={y}, z={z}")

# 字典解包（拆的是键，不是值）
d = {"name": "李四", "age": 30, "city": "北京"}
k1, k2, k3 = d
print(f"字典解包得到的是键：{k1}, {k2}, {k3}")


# ============================================================
# 2. 交换变量
# ============================================================
print("\n" + "=" * 40)
print("2. 交换变量")
print("=" * 40)

a, b = 1, 100
print(f"交换前：a={a}, b={b}")
a, b = b, a
print(f"交换后：a={a}, b={b}")


# ============================================================
# 3. _ 占位符
# ============================================================
print("\n" + "=" * 40)
print("3. _ 占位符——忽略不需要的值")
print("=" * 40)

# 只取名字和城市，中间年龄不要
name, _, city = get_user()
print(f"name={name}, city={city}（年龄被忽略）")


# ============================================================
# 4. * 剩余解包
# ============================================================
print("\n" + "=" * 40)
print("4. * 剩余解包")
print("=" * 40)

# 首 + 中间 + 尾
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# 只取首尾
head, *_, tail = [10, 20, 30, 40, 50]
print(f"head={head}, tail={tail}（中间被忽略）")

# 实战模拟：一行数据，第一列是姓名，最后一列是总分
row = ["张三", "92", "88", "75", "255"]
name, *scores, total = row
print(f"\n实战-成绩处理：name={name}, scores={scores}, total={total}")
# scores 还是字符串，可以转 int 求平均
int_scores = [int(s) for s in scores]
print(f"各科成绩（int）：{int_scores}，平均分：{sum(int_scores)/len(int_scores):.1f}")


# ============================================================
# 5. 嵌套解包
# ============================================================
print("\n" + "=" * 40)
print("5. 嵌套解包")
print("=" * 40)

data = [1, (2, 3), 4]
a, (b, c), d = data
print(f"a={a}, b={b}, c={c}, d={d}")


# ============================================================
# 6. *args 和 **kwargs——函数定义时收包
# ============================================================
print("\n" + "=" * 40)
print("6. *args / **kwargs——收包")
print("=" * 40)

def show_args(*args, **kwargs):
    print(f"  args={args}")
    print(f"  kwargs={kwargs}")

print("调用 show_args(1, 2, 3, a=4, b=5)：")
show_args(1, 2, 3, a=4, b=5)

print("\n什么都不传：")
show_args()


# ============================================================
# 7. 函数调用时解包（和上面的对称）
# ============================================================
print("\n" + "=" * 40)
print("7. 调用时解包——对称操作")
print("=" * 40)

def add(a, b, c):
    return a + b + c

# * 解包列表为位置参数
nums = [1, 2, 3]
result = add(*nums)
print(f"add(*[1,2,3]) = {result}")

# ** 解包字典为关键字参数
info = {"a": 10, "b": 20, "c": 30}
result = add(**info)
print(f"add(**{{'a':10,'b':20,'c':30}}) = {result}")


# ============================================================
# 8. 对称关系：收包 vs 解包（最核心的实战场景）
# ============================================================
print("\n" + "=" * 40)
print("8. 对称关系——装饰器中的 *args, **kwargs")
print("=" * 40)

def logger(func):
    def wrapper(*args, **kwargs):           # ← 收包：不管什么参数都接住
        print(f"  调用 {func.__name__}，参数：args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)      # ← 解包：原封不动传进去
        print(f"  返回：{result}")
        return result
    return wrapper

@logger
def multiply(x, y):
    return x * y

@logger
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

print("调用 multiply(3, 4)：")
multiply(3, 4)

print("\n调用 greet('张三')：")
greet("张三")

print("\n调用 greet('李四', greeting='Hi')：")
greet("李四", greeting="Hi")


# ============================================================
# 9. 解包是传引用
# ============================================================
print("\n" + "=" * 40)
print("9. 解包是传引用，不是拷贝")
print("=" * 40)

inner = [1, 2]
data = [inner, 99]
a, b = data          # a 拿到的是 inner 的地址

print(f"修改前 inner = {inner}")
a.append(888)
print(f"修改后 inner = {inner}  ← 通过 a 修改会影响原来的列表")

print(f"\n⚠️  想独立？用 copy()：")
inner2 = [1, 2]
data2 = [inner2, 99]
a, b = data2
a = a.copy()         # 先拷贝再操作
a.append(888)
print(f"inner2 = {inner2}  ← 不受影响")
print(f"a = {a}")


# ============================================================
# 10. 实战场景：zip + 解包
# ============================================================
print("\n" + "=" * 40)
print("10. 实战：zip + 解包 + 推导式 组合")
print("=" * 40)

names = ["王五", "赵六", "孙七"]
scores = [78, 95, 82]
grades = ["C", "A", "B"]

print("同时遍历三个列表：")
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score}分 ({grade})")

print("\n转成字典：")
result = {name: score for name, score in zip(names, scores)}
print(f"  {result}")


# ============================================================
# ✅ 完成
# ============================================================
print("\n" + "=" * 40)
print("✅ 全部完成！")
print("=" * 40)
