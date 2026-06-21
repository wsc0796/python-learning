---
aliases:
  - 21-list-deep
---
# 列表深入操作

> 前置：已掌握列表基本用法
> 目标：覆盖列表所有常用操作
> 用时：约 8 分钟
>
> 相关笔记：[切片操作](../02-slice/theory_02_slice.md) · [元组与集合](../17-tuple-set/theory_17_tuple_set.md) · [字典 dict](../06-dict/theory_06_dict.md)

---

## 一、增删改查

```python
lst = [1, 2, 3]

# 增
lst.append(4)         # [1, 2, 3, 4]      末尾添加
lst.insert(1, 99)     # [1, 99, 2, 3, 4]  指定位置插入
lst.extend([5, 6])    # [1, 99, 2, 3, 4, 5, 6]  合并另一个列表

# 删
lst.pop()             # 返回 6，lst = [1, 99, 2, 3, 4, 5]  删末尾
lst.pop(1)            # 返回 99，lst = [1, 2, 3, 4, 5]     删指定索引
lst.remove(3)         # lst = [1, 2, 4, 5]                 删第一个匹配的值
# lst.remove(999)     # ❌ ValueError — 不存在会报错
lst.clear()           # lst = []                            清空

# 改
lst = [1, 2, 3]
lst[1] = 99           # [1, 99, 3]

# 查
lst = [10, 20, 30, 20, 40]
print(lst.index(20))    # 1  第一次出现的位置
print(lst.index(20, 2)) # 3  从索引2开始找20
print(lst.count(20))    # 2  出现次数
print(30 in lst)        # True
```

## 二、排序和反转

```python
# sort() 原地排序
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)          # [1, 1, 3, 4, 5]

nums.sort(reverse=True)
print(nums)          # [5, 4, 3, 1, 1]

# sorted() 返回新列表
nums = [3, 1, 4]
sorted_nums = sorted(nums)
print(sorted_nums)   # [1, 3, 4]
print(nums)          # [3, 1, 4] — 原列表不变

# reverse() 反转
nums.reverse()
print(nums)          # [4, 1, 3]

# 用 key 排序（已讲，复习一下）
students = [("张三", 92), ("李四", 88), ("王五", 95)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)  # [('王五', 95), ('张三', 92), ('李四', 88)]
```

## 三、列表复制

```python
# 浅复制
a = [1, 2, 3]
b = a.copy()        # ✅
c = a[:]            # ✅ 等价
d = list(a)         # ✅ 等价

a[0] = 99
print(b[0])         # 1 — 不受影响

# 但浅复制对于嵌套列表有问题
a = [[1, 2], [3, 4]]
b = a.copy()
a[0][0] = 99
print(b[0][0])      # 99 — 内层列表还是共享的！
```

## 四、列表嵌套

```python
# 二维列表（矩阵）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])   # 6 — 第2行第3列

# 遍历
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
```

## 五、列表常用函数

```python
nums = [3, 1, 4, 1, 5]
print(len(nums))       # 5
print(max(nums))       # 5
print(min(nums))       # 1
print(sum(nums))       # 14
print(any(x > 4 for x in nums))   # True
print(all(x > 0 for x in nums))   # True
```

## 备考相关

- [[EXAM_PREP/day02/00_今日任务]] — Day 2 字符串与组合数据类型
- [[EXAM_PREP/day07/00_今日任务]] — Day 7 学生管理系统综合题
