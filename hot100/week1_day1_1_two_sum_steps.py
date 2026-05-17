"""
1. 两数之和 — 拆解版
================================================================
Step 1 — 一句话核心技巧
================================================================

哈希表存"差值"：遍历时查 target - nums[i] 在不在表里。

什么意思？
  比如 nums=[3,2,4], target=6
  你手上拿着 3，想找 6-3=3，有没有另外一个 3？
  你手上拿着 2，想找 6-2=4，后面有没有 4？
  你手上拿着 4，想找 6-4=2，前面有没有 2？—— 找到了！

关键思维：
  不用两两配对（O(n²)），而是把"见过的数"存起来，
  每遍历一个新数就问："有没有人和我配对？"
  查表操作是 O(1)，总时间降为 O(n)。

================================================================
Step 2 — 拆解成独立知识点
================================================================
"""

# ─── 2a: 字典的 in 判断 — "有没有这个 key？" ───

phonebook = {
    "张三": "13800001111",
    "李四": "13900002222",
}

# in 操作是在字典的 key 里查找，不是 value
print("张三" in phonebook)    # True
print("王五" in phonebook)    # False
print("13800001111" in phonebook)  # False ← 这是value不是key！


# ─── 2b: dict[key] 取值 和 dict[key] = value 存值 ───

# 存
phonebook["王五"] = "13600003333"

# 取
print(phonebook["张三"])      # 13800001111

# 取不存在的 key 会报错
# print(phonebook["赵六"])    # KeyError!

# 安全的取法：先 in 判断，再取
if "赵六" in phonebook:
    print(phonebook["赵六"])


# ─── 2c: enumerate 同时取下标和值 ───

fruits = ["苹果", "香蕉", "橘子"]
for i, fruit in enumerate(fruits):
    print(f"下标{i} = {fruit}")

# 输出：
#   下标0 = 苹果
#   下标1 = 香蕉
#   下标2 = 橘子


# ─── 2d: target - num 就是"要找的另一个数" ───

nums = [3, 2, 4]
target = 6

# 当你遍历到第一个数 3 时：
num = 3
other = target - num          # 6 - 3 = 3
print(f"当前拿到{num}，需要找{other}")   # 需要找3

# 当你遍历到第二个数 2 时：
num = 2
other = target - num          # 6 - 2 = 4
print(f"当前拿到{num}，需要找{other}")   # 需要找4


# ================================================================
# Step 3 — 手动模拟过程
# ================================================================

# 例子：nums = [3, 2, 4], target = 6
# 期待结果：下标 [1, 2]（2 + 4 = 6）

# 下面一行行手写模拟，不用循环：

seen = {}                           # 空哈希表

# — 第1步：i=0, num=3 —
other = 6 - 3                       # 3
print(f"i=0, num=3, 需要找{other}")  # 需要找3
# seen 是 {}，没有 3
if 3 in seen:
    print("找到了！")
else:
    print("没找到，把3存进去")
    seen[3] = 0                      # seen = {3: 0}

# — 第2步：i=1, num=2 —
other = 6 - 2                       # 4
print(f"i=1, num=2, 需要找{other}")  # 需要找4
# seen 是 {3: 0}，没有 4
if 4 in seen:
    print("找到了！")
else:
    print("没找到，把2存进去")
    seen[2] = 1                      # seen = {3: 0, 2: 1}

# — 第3步：i=2, num=4 —
other = 6 - 4                       # 2
print(f"i=2, num=4, 需要找{other}")  # 需要找2
# seen 是 {3: 0, 2: 1}，有 2！
if 2 in seen:
    print(f"找到了！下标 [{seen[2]}, {2}]")   # [1, 2]
else:
    print("没找到")

"""
手动模拟完了，看懂了的话，回答一个问题：
  为什么第3步找到的是下标[1, 2]？
  因为 seen[2] 是第2步存的，值是 1（下标）
  当前是第3步，下标是 2
  所以 [seen[2], 2] = [1, 2]
"""

# ================================================================
# Step 4 — 组装成循环
# ================================================================

def two_sum(nums: list[int], target: int) -> list[int]:
    """把上面手写的过程变成循环"""
    seen = {}
    for i, num in enumerate(nums):     # 遍历，同时取下标和值
        other = target - num           # 需要找的另一个数
        if other in seen:              # 另一个数之前出现过？
            return [seen[other], i]    # 返回[另一个的下标, 当前下标]
        seen[num] = i                  # 没找到，把自己记下来
    return []

# 测试
print(two_sum([3, 2, 4], 6))    # [1, 2]
print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 3], 6))      # [0, 1]


# ================================================================
# Step 5 — 你的练习（填空）
# ================================================================

def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    """
    暴力法版本：两重循环，不用哈希表
    虽然慢（O(n²)），但不用理解哈希表也能写
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # TODO: 填条件
                return [i, j]
    return []


if  __name__== "__main__":
    # 验证暴力法
    print(two_sum_bruteforce([3, 2, 4], 6))       # [1, 2]
    print(two_sum_bruteforce([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum_bruteforce([3, 3], 6))          # [0, 1]


# ================================================================
# 相关 Python 笔记
# ================================================================
# dict 基础 → ../06-dict/theory_06_dict.md  （第1节：创建/增删改查）
#          → ../06-dict/practice_06_dict.py （练习1-3）
# enumerate → ../02-slice/ （enumerate 是遍历的常用方式）
