---
aliases:
  - 06-dict
---
# 06 — 字典 dict

> 相关笔记：[列表深入操作](../21-list-deep/theory_21_list_deep.md) · [元组与集合](../17-tuple-set/theory_17_tuple_set.md)

## 一句话

字典是 **key→value** 的映射表，类似"查电话号码"：给你人名（key），找到号码（value）。

```python
phone = {"张三": "138xxxx", "李四": "139xxxx"}
print(phone["张三"])   # 138xxxx
```

## 1. 创建字典

```python
# 方式1：花括号
d1 = {"name": "小明", "age": 18}

# 方式2：dict() 构造
d2 = dict(name="小明", age=18)     # 注意！key 不用加引号

# 方式3：空字典
d3 = {}
d4 = dict()
```

## 2. 增删改查

```python
d = {}

# 增 / 改（key不存在=增，key已存在=改）
d["name"] = "小明"        # {"name": "小明"}
d["age"] = 18             # {"name": "小明", "age": 18}
d["name"] = "小红"        # {"name": "小红", "age": 18}  ← 改

# 查（两种方式）
print(d["name"])           # "小红"    ← key存在就返回值
# print(d["gender"])       # KeyError! ← key不存在直接报错

print(d.get("name"))       # "小红"    ← 安全的查法
print(d.get("gender"))     # None      ← key不存在返回None，不报错
print(d.get("gender", "未知"))  # "未知"  ← 可以指定默认值

# 判断 key 是否存在
print("name" in d)          # True
print("gender" in d)        # False

# 删除
del d["age"]                # {"name": "小红"}
# del d["gender"]           # KeyError! 不存在会报错
```

## 3. 遍历字典

```python
d = {"a": 1, "b": 2, "c": 3}

# 遍历 key（默认）
for k in d:
    print(k, d[k])          # a 1 / b 2 / c 3

# 遍历 key-value
for k, v in d.items():
    print(k, v)             # a 1 / b 2 / c 3

# 只遍历 value
for v in d.values():
    print(v)                # 1 / 2 / 3
```

## 4. 典型用法：分组（Group By）

这是 Hot100 最常用的模式：

```python
groups = {}                # key=某个标准, value=列表

for word in ["eat", "tea", "tan"]:
    key = "aet"            # 排序后的标准形式
    if key not in groups:  # 第一次出现→初始化
        groups[key] = []
    groups[key].append(word)  # 加入分组

print(groups)
# {"aet": ["eat", "tea"], "ant": ["tan"]}
```

## 5. 注意事项

| 场景 | 正确写法 | 错误写法 |
|------|---------|---------|
| key 不存在时取值 | `d.get(key)` 或 `if k in d:` | `d[key]` 直接取 |
| 保证 key 存在 | `d.setdefault(key, [])` | 手动 if 判断（也行） |
| 删除不存在的 key | `if k in d: del d[k]` | `del d[k]` 直接删 |

## Hot100 关联

遇到 dict 用法的题目：
- **第1题** 两数之和 → 存差值，O(1) 查找
- **第49题** 字母异位词分组 → 排序后分组
- **第128题** 最长连续序列 → 集合判断存在
