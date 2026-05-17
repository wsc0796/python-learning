---
aliases:
  - 04-listcomp-class
---
# Day 4：列表推导式 + lambda + 类/继承

读完约 10 分钟（分两次读也行）。

---

## 一、列表推导式（Day2 补课，今天应该先学这个）

你之前学过了循环：

```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
# squares = [1, 4, 9, 16, 25]
```

列表推导式是同一个逻辑的简写：

```python
squares = [x ** 2 for x in range(1, 6)]
# 结果完全相同：[1, 4, 9, 16, 25]
```

**语法拆解：**

```
[对x做什么   for x in 可迭代对象   要不要过滤]
  ↑                ↑                   ↑
 x ** 2       for x in range(1,6)     (可选)
```

### 带过滤的

```python
# 原版循环
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# 推导式
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

### Java 对照：Stream API

```java
// Java
List<Integer> squares = IntStream.range(1, 6)
    .map(x -> x * x)
    .boxed()
    .collect(Collectors.toList());
```

```python
# Python 推导式
squares = [x ** 2 for x in range(1, 6)]
```

推导式更简洁，但不要写太复杂——**超过一层 for 就回去写普通循环。**

---

## 二、lambda：匿名函数

### 什么时候用

```python
# 普通函数：有名字，可以反复调用
def square(x):
    return x ** 2

# lambda：没名字，用完就扔
lambda x: x ** 2
```

**lambda 只在你需要一个「只用一次的小函数」时用。** 能写 def 就写 def，别硬用 lambda。

### 语法

```
lambda 参数: 返回值表达式
```

只能写**一个表达式**（不能写多行、不能写 return、不能写 if 语句）。

### 配合 map/filter 使用

```python
nums = [1, 2, 3, 4, 5]

# map：对每个元素做操作
list(map(lambda x: x ** 2, nums))
# [1, 4, 9, 16, 25]

# filter：保留满足条件的
list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]
```

**但说实话：** 列表推导式比 map/filter 更 Pythonic：

```python
# 不推荐
list(map(lambda x: x ** 2, nums))

# 推荐
[x ** 2 for x in nums]
```

结论：了解 lambda 是什么就行，日常能用推导式就用推导式。

---

## 三、类/继承：你有 Java 基础，这节很快

### Python 的类 vs Java 的类

```java
// Java
public class Dog {
    private String name;

    public Dog(String name) {
        this.name = name;
    }

    public void bark() {
        System.out.println(this.name + " 汪汪");
    }
}

Dog d = new Dog("旺财");
d.bark();
```

```python
# Python
class Dog:
    def __init__(self, name):      # 构造函数，等于 Java 的 Dog(String name)
        self.name = name

    def bark(self):                 # 方法，self 等于 Java 的 this
        print(f"{self.name} 汪汪")

d = Dog("旺财")
d.bark()
```

### 一一对应

| Java | Python | 说明 |
|------|--------|------|
| `class Dog {}` | `class Dog:` | 定义类，Python 用冒号不用花括号 |
| `public Dog(...)` | `def __init__(self, ...)` | 构造函数 |
| `this.name` | `self.name` | 当前实例的成员变量 |
| `new Dog()` | `Dog()` | 创建实例，Python 不需要 new |
| `void bark()` | `def bark(self):` | 方法，self 必须显式写在参数里 |

### 你唯一要适应的：`self` 必须显式写

```python
class Counter:
    def __init__(self):
        self.count = 0       # 初始化成员变量

    def add(self, n):
        self.count += n      # 用 self.count 访问

    def show(self):
        print(f"当前计数：{self.count}")

c = Counter()
c.add(5)
c.add(3)
c.show()    # 当前计数：8
```

**Java 里 this 是可写可不写的（除非重名），Python 里 self 必须写。** 这是最大的习惯差异。

### 继承

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):              # ← 继承用括号，等于 Java 的 extends
    def speak(self):            # 重写父类方法
        return f"{self.name} 汪汪"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵"

d = Dog("旺财")
c = Cat("咪咪")
print(d.speak())   # 旺财 汪汪
print(c.speak())   # 咪咪 喵喵
```

**跟 Java 一样：** 继承 → 重写方法 → 多态。

---

## 当前级别许可

| 内容 | 状态 |
|------|------|
| 列表推导式 | ⚠️ 今天学完切片后可以碰，但只做简单推导式 |
| lambda | ⚠️ 了解即可，不要求手写熟练 |
| map/filter | ⚠️ 了解即可，日常用推导式代替 |
| 类/__init__/self | ✅ 今天可以学（Java基础好，这节很快） |
| 继承 | ✅ 今天可以学 |

相关笔记：[列表深入操作](../21-list-deep/theory_21_list_deep.md) · [推导式进阶 · any/all/sorted](../16-python-gaps/theory_16_python_gaps.md)
