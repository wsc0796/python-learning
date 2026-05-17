"""
11. 盛最多水的容器 (Container With Most Water)

================================================================
Step 1 — 一句话核心技巧
================================================================

双指针从两端向中间收缩，哪边矮就移动哪边。

为什么？
  容器的水量 = min(左高, 右高) × 宽度
  移动高的那边 → 宽度变小，高度不会变高 → 水量一定减小 ❌
  移动矮的那边 → 宽度变小，但高度可能变高 → 水量可能增大 ✅

================================================================
Step 2 — 拆解知识点
================================================================
"""

# ─── 2a: min() 取最小值 ───
print(min(3, 7))        # 3
print(min(5, 2, 9))     # 2

# ─── 2b: 双指针同时从两端走 ───
nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left = 0
right = len(nums) - 1   # 8

print(f"左指针指向 {nums[left]} (下标{left})")
print(f"右指针指向 {nums[right]} (下标{right})")

# ─── 2c: 计算面积 ───
height = min(nums[left], nums[right])   # min(1, 7) = 1
width = right - left                    # 8 - 0 = 8
area = height * width                   # 1 * 8 = 8
print(f"当前面积: {height} × {width} = {area}")


# ================================================================
# Step 3 — 手动模拟过程
# ================================================================

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# 手动模拟，不用循环
left = 0
right = len(height) - 1
max_area = 0

# 第1步：left=0(1), right=8(7)
h = min(height[left], height[right])     # min(1, 7) = 1
w = right - left                          # 8
area = h * w                              # 8
print(f"left={left}({height[left]}), right={right}({height[right]}) → 面积={area}")
max_area = max(max_area, area)
# 1 < 7，左指针右移
left += 1

# 第2步：left=1(8), right=8(7)
h = min(height[left], height[right])     # min(8, 7) = 7
w = right - left                          # 7
area = h * w                              # 49
print(f"left={left}({height[left]}), right={right}({height[right]}) → 面积={area}")
max_area = max(max_area, area)
# 8 > 7，右指针左移
right -= 1

# 第3步：left=1(8), right=7(3)
h = min(height[left], height[right])     # min(8, 3) = 3
w = right - left                          # 6
area = h * w                              # 18
print(f"left={left}({height[left]}), right={right}({height[right]}) → 面积={area}")
max_area = max(max_area, area)
# 8 > 3，右指针左移
right -= 1

print(f"手动模拟最大面积: {max_area}")


# ================================================================
# Step 4 — 组装成循环
# ================================================================

def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1          # 左边矮 → 左指针右移
        else:
            right -= 1         # 右边矮/相等 → 右指针左移

    return max_area

# 测试
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
print(max_area([1, 1]))                          # 1


# ================================================================
# Step 5 — 你的练习（填空）
# ================================================================

def max_area_bruteforce(height: list[int]) -> int:
    """
    暴力法：两重循环，计算所有组合的面积
    输入 height = [1, 8, 6, 2]
    计算:
      (0,1): min(1,8)*1=1  (0,2): min(1,6)*2=2  (0,3): min(1,2)*3=3
      (1,2): min(8,6)*1=6  (1,3): min(8,2)*2=4
      (2,3): min(6,2)*1=2
    最大 = 6
    """
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            # TODO: 计算面积并更新 max_area
            pass
    return max_area


if __name__ == "__main__":
    print("\n=== 暴力法验证 ===")
    print(max_area_bruteforce([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
    print(max_area_bruteforce([1, 1]))                          # 1


# ================================================================
# 相关 Python 笔记
# ================================================================
# 双指针 → 这是 Hot100 的常见模式，不需要额外语法知识
