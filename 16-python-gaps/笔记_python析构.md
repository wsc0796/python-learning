---
aliases:
  - python-析构
  - __del__方法
  - 垃圾回收
  - 对象销毁
  - destructor
---

# Python 析构：`__del__`、引用计数、垃圾回收

> Python 对象什么时候死？`del` 到底删了什么？为什么析构函数不可靠？
> 读完约 15 分钟。推荐先读 [[../17-context-iterator-async/01-context-manager]]。

---

## 一、先纠正一个常见误解

> ❌ **错误认知**：`del obj` = 立即调用 `__del__`，对象当场销毁。
> ✅ **正确认知**：`del` 只是**删除一个引用**。当对象引用计数归零时，`__del__` 才被调用。

```python
a = [1, 2, 3]
b = a            # 现在 [1,2,3] 有 2 个引用

del a            # 删除变量 a，但引用只少了一个
                 # [1,2,3] 还有 b 在引用它 → __del__ 不会触发

del b            # 最后一个引用删掉 → 引用计数归零
                 # 现在 Python 才会销毁这个 list
```

Java/Spring 类比：

| Java | Python |
|------|--------|
| 对象没引用 → GC 在未来某个时刻回收 | 对象没引用 → **立刻**回收（引用计数归零时） |
| `finalize()` — 不确定何时执行 | `__del__` — 引用计数归零时**立刻**执行 |
| 堆外资源靠 `try-with-resources` | 资源靠 `with` 语句 + 上下文管理器 |

---

## 二、引用计数：Python 怎么知道一个对象"没人用了"

### Python 内部为每个对象维护一个计数器

```python
import sys

class Demo:
    pass

d = Demo()
print(sys.getrefcount(d))   # 2（d 变量 + getrefcount 的临时参数）

d2 = d
print(sys.getrefcount(d))   # 3（多了一个引用）

del d2
print(sys.getrefcount(d))   # 2（引用减回去了）
```

### 引用从哪来

| 操作 | 效果 |
|------|------|
| `a = obj` | 引用 +1 |
| `lst.append(obj)` | 引用 +1 |
| `d[key] = obj` | 引用 +1 |
| 函数传参 | 临时引用 +1（函数结束后 -1） |
| `del a` | 引用 -1 |
| 离开作用域 | 局部变量引用 -1 |
| 重新赋值 `a = other` | 旧对象引用 -1，新对象引用 +1 |

> `getrefcount()` 本身也会增加一个临时引用，所以返回值通常比预期多 1。

---

## 三、`__del__`：析构方法

### 定义

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"创建 {name}")

    def __del__(self):
        print(f"销毁 {self.name}")
```

### 触发时机

```python
r = Resource("A")
r2 = r
del r          # 只删了一个引用，不会触发 __del__
print("---")
del r2         # 最后一个引用也没了 → 触发 __del__
# 输出：
# 创建 A
# ---
# 销毁 A
```

**核心规则**：`__del__` 只在引用计数归零、解释器即将回收对象时调用。不是 `del` 触发的，是"没人引用这个对象了"触发的。

### 程序结束时也会触发

```python
r = Resource("全局对象")
# 程序结束，所有变量自动销毁
# 输出：销毁 全局对象
```

---

## 四、`__del__` 最大的坑：循环引用

### 问题：两个对象互相引用 → 永远无法归零

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.friend = None

    def __del__(self):
        print(f"销毁 {self.name}")

a = Node("A")
b = Node("B")
a.friend = b       # A 引用 B
b.friend = a       # B 引用 A

del a
del b              # 两个对象的引用计数都是 1（对方持有）→ 都不归零
# __del__ 不会被调用！
```

**这就是为什么 Python 不只有引用计数，还有垃圾回收器。**

---

## 五、垃圾回收（GC）：专门解决循环引用

### `gc` 模块

```python
import gc

# 手动触发 GC
gc.collect()       # 扫描所有对象，找到循环引用，打破它
```

Python 的 GC 采用**分代回收**策略：
- 年轻代（generation 0）：新对象，频繁扫描
- 中年代（generation 1）：活过一轮的对象
- 老年代（generation 2）：长期存活的对象

```python
import gc
print(gc.get_count())    # (年轻代活跃数, 中年代活跃数, 老年代活跃数)
print(gc.get_threshold())  # (700, 10, 10) — 触发 GC 的阈值
```

### 检测循环引用

```python
import gc

gc.set_debug(gc.DEBUG_SAVEALL)   # 回收时保留对象

# 创建循环引用
a = Node("A")
b = Node("B")
a.friend = b
b.friend = a

del a, b
gc.collect()    # 手动回收
print(gc.garbage)  # 查看无法回收的对象
```

### 循环引用里 `__del__` 不会被调用

这是 Python 的设计决定：有 `__del__` 的循环引用对象，GC **不敢**贸然回收，因为不知道该先销毁哪个。这些对象会永久堆在 `gc.garbage` 里，直到你手动处理。

**结论**：别在 `__del__` 里写关键清理逻辑。

---

## 六、正确的资源管理：用 `with`，不是 `__del__`

`__del__` 的最大问题是：你不知道它什么时候执行。

| 方式 | 时机 | 可靠性 |
|------|------|--------|
| `__del__` | 引用计数归零后 | ❌ 循环引用时永远不触发 |
| `try...finally` | 代码块结束时 | ✅ 一定执行 |
| `with` + `__exit__` | `with` 块结束时 | ✅ 一定执行 |

```python
# 不推荐：靠 __del__ 关闭文件
class BadFile:
    def __init__(self, path):
        self.f = open(path, "w")

    def __del__(self):
        self.f.close()         # 循环引用时永远不会执行 → 文件泄漏

# 推荐：用上下文管理器
class GoodFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.f = open(self.path, "w")
        return self.f

    def __exit__(self, *args):
        self.f.close()         # with 结束一定执行

with GoodFile("data.txt") as f:
    f.write("hello")
# f 已关闭，100% 保证
```

上下文管理器详见：[[../17-context-iterator-async/01-context-manager]]

---

## 七、`del` 语句的其他用法

### 删除变量

```python
x = 10
del x       # 删除变量名 x，值 10 的引用计数减 1
# print(x)  # NameError: x 不存在了
```

### 删除列表元素

```python
lst = ["a", "b", "c"]
del lst[1]      # ['a', 'c']
del lst[0:2]    # 删除切片
```

### 删除字典键

```python
d = {"name": "tom", "age": 20}
del d["age"]    # {'name': 'tom'}
```

### 删除属性

```python
class Demo:
    def __init__(self):
        self.x = 1

obj = Demo()
del obj.x       # obj 没有 x 属性了
```

> `del` 的本质：**删除一个名字 / 索引 / 键 / 属性**，让目标对象的引用计数减 1。被引用的对象是否销毁，取决于引用计数是否归零。

---

## 八、总结：什么时候用哪个

| 场景 | 用什么 | 原因 |
|------|--------|------|
| 文件、数据库连接、锁 | `with` 语句 | 确定性的清理，异常也保证执行 |
| 临时状态恢复 | `@contextmanager` | 写起来最简洁 |
| 缓存清理 / 统计计数 | `__del__` | 可以，但仅限无循环引用的场景 |
| 关键资源（永远不要！） | ~~`__del__`~~ | 循环引用 = 哑巴亏 |

### 一句话

> Python 的 `__del__` 是**不可靠的析构函数**。管理资源用 `with`，别指望析构函数。

---

## 九、快速自测

1. `del obj` 之后，对象一定被销毁了吗？为什么？
2. `sys.getrefcount(obj)` 返回 3，实际引用计数是几？
3. 两个对象互相引用，`del` 掉所有外部引用后，`__del__` 会被调用吗？
4. 文件关闭应该放在 `__del__` 里还是 `__exit__` 里？为什么？
