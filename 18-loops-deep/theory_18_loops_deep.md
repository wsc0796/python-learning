---
aliases:
  - 18-loops-deep
---
# 循环深入：while、for、break、continue、循环与 else

> 前置：已掌握 if 和基本 for/while 用法
> 目标：覆盖循环所有细节
> 用时：约 8 分钟
>
> 相关笔记：[条件语句](../23-if-conditionals/theory_23_if_conditionals.md) · [列表遍历操作](../21-list-deep/theory_21_list_deep.md)

---

## 一、while 循环

```python
# 基本结构
count = 0
while count < 5:
    print(count)
    count += 1
# 0 1 2 3 4

# 累加求和
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)   # 5050
```

## 二、for 循环

```python
# 遍历范围
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):     # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(1, 10, 2): # 1, 3, 5, 7, 9（步长2）
    print(i)

# 遍历可迭代对象
for ch in "hello":        # h e l l o
    print(ch)

for item in [1, 2, 3]:    # 1 2 3
    print(item)
```

## 三、break 和 continue

```python
# break：跳出整个循环
for i in range(10):
    if i == 5:
        break
    print(i)      # 0 1 2 3 4

# continue：跳过当前次，继续下次
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)      # 1 3 5 7 9
```

## 四、循环与 else（Python 独有）

```python
# else 块：循环正常结束时执行（没有被 break 中断）

# 例1：查找元素
nums = [1, 3, 5, 7, 9]
target = 4

for n in nums:
    if n == target:
        print("找到了")
        break
else:
    print("没找到")   # 只有没 break 时才执行

# 例2：判断素数
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} 不是素数")
        break
else:
    print(f"{num} 是素数")  # 没被整除 → 是素数
```

**while-else 也一样**：
```python
count = 0
while count < 5:
    if count == 3:
        break
    count += 1
else:
    print("循环完整结束")  # 不会执行，因为 break 了
print(count)  # 3
```

## 五、循环嵌套

```python
# 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()  # 换行
```

## 一句话记

> `break` 跳出整个循环，`continue` 跳过当前次。`else` 在循环没被 `break` 时才执行。

---

## 备考相关

- [[EXAM_PREP/day01/00_今日任务]] — Day 1 基础语法与流程控制
- [[EXAM_PREP/day07/00_今日任务]] — Day 7 学生管理系统综合题
