# 双指针 — 4 道题吃透

读完约 10 分钟。

---

## 核心模式

> 两个指针从不同位置出发，按某种规则移动，将 O(n²) 暴力降为 O(n)。

## 难度递进

```
283.移动零（快慢指针）  → O(n) 交换
  ↓
11.盛水容器（左右对撞） → 每次舍弃较矮的边
  ↓
15.三数之和（固定+对撞）→ O(n²) → O(n²)，排序去重
  ↓
42.接雨水（左右对撞）   → 边移动边算，一次遍历
```

---

## 283. 移动零（简单）

**思路：** 快慢指针，快指针探路，遇到非零就跟慢指针交换。

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                int temp = nums[fast];
                nums[fast] = nums[slow];
                nums[slow] = temp;
                slow++;
            }
        }
    }
}
```

---

## 11. 盛最多水的容器（中等）

**思路：** 左右对撞，每次移动高度较小的那一边（短板决定水量）。

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1, max = 0;
        while (left < right) {
            int area = (right - left) * Math.min(height[left], height[right]);
            max = Math.max(max, area);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return max;
    }
}
```

---

## 15. 三数之和（中等）

**思路：** 排序 + 固定一个数，剩下两个用对撞指针找两数之和。

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;  // 去重
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    while (j < k && nums[j] == nums[j + 1]) j++;  // 去重
                    while (j < k && nums[k] == nums[k - 1]) k--;  // 去重
                    j++; k--;
                } else if (sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return res;
    }
}
```

---

## 42. 接雨水（困难）

**思路：** 左右对撞，用 `leftMax` 和 `rightMax` 记录两侧最高柱子，边移动边算。

```java
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length <= 2) return 0;

        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int water = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
            }
        }
        return water;
    }
}
```

---

## 速记口诀

> 快慢指针移**零**，左右对撞求**水**，
> 短板决定**容器**，排序固一去**三数**。
>
> 核心就一句话：**谁小移动谁。**

| 题目 | 指针类型 | 移动规则 | 复杂度 |
|------|---------|---------|--------|
| 283 移动零 | 快慢（同向） | fast 探路，非零交换 | O(n) |
| 11 盛水容器 | 左右对撞 | 移较矮的一边 | O(n) |
| 15 三数之和 | 固定+对撞 | sum<0 左移，>0 右移 | O(n²) |
| 42 接雨水 | 左右对撞 | 移 leftMax/rightMax 更小的一边 | O(n) |
