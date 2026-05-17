"""
1. 两数之和 — 完整版代码
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """哈希表法：key=数组值，value=下标"""
    seen = {}                          # key: 数字, value: 下标
    for i, num in enumerate(nums):     # i=下标, num=值
        other = target - num           # 需要找的另一个数
        if other in seen:              # 找到了！
            return [seen[other], i]    # [另一个数的下标, 当前下标]
        seen[num] = i                  # 没找到，把自己存进去
    return []                          # 题目保证有解，这里不会执行到
