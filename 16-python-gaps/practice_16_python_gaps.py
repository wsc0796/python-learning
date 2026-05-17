"""
16 — Python 基础补漏练习
None/真值 · is vs == · 可变/不可变 · *args **kwargs · enumerate/zip · 推导式 · if __name__
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ============================================================
# 练习1：None 和真值
# ============================================================
# TODO: 补全函数，判断输入值是否为"假"

def is_falsy(value) -> bool:
    """返回 True 如果 value 是假值（False、None、0、""、[]、{}）"""
    return not value

# 验证
print("--- 真值测试 ---")
print(is_falsy(None))      # True
print(is_falsy(0))         # True
print(is_falsy(""))        # True
print(is_falsy([]))        # True
print(is_falsy("abc"))     # False
print(is_falsy([1, 2]))    # False


# ============================================================
# 练习2：is vs ==
# ============================================================
# TODO: 先猜再跑，看每组的结果

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("\n--- is vs == ---")
print(a == b)    # ？  true
print(a is b)    # ？    false
print(a is c)    # ？    true
# 思考：为什么 is 和 == 结果不同？什么情况下 is 返回 True？


# ============================================================
# 练习3：可变对象的陷阱
# ============================================================
# TODO: 先猜输出，然后取消注释跑

def add_student(name, students=[]):     # 这里有问题
    students.append(name)
    return students

print("\n--- 默认参数陷阱 ---")
print(add_student("张三"))    # ?
print(add_student("李四"))    # ?（期望只是 ["李四"] 吗？）
print(add_student("王五"))    # ?

# TODO: 修改上面的函数，修复默认参数问题
# 提示：用 None 做默认值


# ============================================================
# 练习4：*args 和 **kwargs
# ============================================================

# TODO 4a: 写一个函数 sum_all(*args) 求所有参数的和
def sum_all(*args):
    return sum(args)  # 一行搞定


# 验证
print("\n--- *args ---")
print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100


# TODO 4b: 写一个函数 print_info(**kwargs)，打印所有键值对
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 验证
print("\n--- **kwargs ---")
print_info(name="张三", age=25, city="南昌")


# ============================================================
# 练习5：enumerate 和 zip
# ============================================================

# TODO: 用 enumerate 打印带编号的待办事项
todos = ["买早餐", "写作业", "跑步", "背单词"]

print("\n--- enumerate ---")
for i, todo in enumerate(todos, 1):  # TODO: 把 None 改成 1
    print(f"{i}. {todo}")


# TODO: 用 zip 同时遍历名字和分数
names = ["张三", "李四", "王五"]
scores = [92, 88, 75]

print("\n--- zip ---")
for name, score in zip(names, scores):
    print(f"{name}: {score}分")


# ============================================================
# 练习6：字典推导式
# ============================================================

# TODO: 把下面的列表转成 {名字: 分数} 字典
students_list = [("张三", 92), ("李四", 88), ("王五", 75)]
# TODO: 字典推导式 → {'张三': 92, '李四': 88, '王五': 75}
# 格式: {key: value for name, score in students_list}


# ============================================================
# 练习7：if __name__ == "__main__"
# ============================================================

def greet(name):
    return f"你好, {name}"

# TODO: 把下面的测试代码放到 if __name__ == "__main__": 块里
# 这样 import 时不会自动跑
# 参考：print(greet("张三"))


# ============================================================
# ✅ 完成标记
# ============================================================
if __name__ == "__main__":
    print("\n✅ 基础补漏练习完成！")
