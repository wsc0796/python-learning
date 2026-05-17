---
aliases:
  - 27-regex
---
# 正则表达式：re 模块

> 前置：字符串方法、文件读写
> 目标：能用模式匹配验证和提取数据
> 用时：约 15 分钟
>
> 相关笔记：[字符串方法](../24-string-methods/theory_24_string_methods.md) · [条件判断](../23-if-conditionals/theory_23_if_conditionals.md)

---

CS50P 里 David Malan 对正则的定义：*"Regular expressions let you define patterns to validate data or extract specific information from datasets."*

用 Python 的字符串方法也能做验证和提取，但正则**更短、更强大、更标准**。比如验证一个邮箱格式，手写 `if` + `split` 可能需要 10 行，正则一行搞定。

---

## 一、`re.search()` — 查找第一个匹配

```python
import re

# 基本用法
result = re.search(r"Python", "I love Python")
print(result)   # <re.Match object; span=(7, 13), match='Python'>

# 没找到返回 None
result = re.search(r"Java", "I love Python")
print(result)   # None
```

**关键惯例**：模式字符串用 `r"..."`（raw string），避免 `\` 被 Python 当成转义符。写正则时**永远用 raw string**。

---

## 二、元字符 — 正则的核心语法

| 符号 | 含义 | 示例 | 匹配 |
|------|------|------|------|
| `.` | 任意单个字符（除换行） | `r"h.t"` | hot, hat, hit, h@t |
| `*` | 前一个字符重复 0 次或多次 | `r"ho*t"` | ht, hot, hoot |
| `+` | 前一个字符重复 1 次或多次 | `r"ho+t"` | hot, hoot（不匹配 ht） |
| `?` | 前一个字符可选（0 或 1 次） | `r"colou?r"` | color, colour |
| `^` | 字符串开头 | `r"^Hello"` | 以 Hello 开头 |
| `$` | 字符串结尾 | `r"\.com$"` | 以 .com 结尾 |
| `[]` | 字符集合 | `r"[aeiou]"` | 任意一个元音字母 |
| `[^]` | 排除字符集合 | `r"[^0-9]"` | 任意非数字字符 |
| `\|` | 或 | `r"cat\|dog"` | cat 或 dog |

**动手理解：**

```python
# . 匹配任意字符
re.search(r"h.t", "hot")     # ✓
re.search(r"h.t", "h@t")     # ✓
re.search(r"h.t", "ht")      # None — 刚好3个字符

# * 零次或多次
re.search(r"ho*t", "ht")     # ✓  o出现0次
re.search(r"ho*t", "hot")    # ✓  o出现1次
re.search(r"ho*t", "hooot")  # ✓  o出现3次

# + 一次或多次
re.search(r"ho+t", "hot")    # ✓
re.search(r"ho+t", "hooot")  # ✓
re.search(r"ho+t", "ht")     # None — o至少要1次
```

---

## 三、字符类（Character Classes）

| 简写 | 等价于 | 含义 |
|------|--------|------|
| `\w` | `[a-zA-Z0-9_]` | 单词字符（字母、数字、下划线） |
| `\W` | `[^a-zA-Z0-9_]` | 非单词字符 |
| `\d` | `[0-9]` | 数字 |
| `\D` | `[^0-9]` | 非数字 |
| `\s` | `[ \t\n\r\f\v]` | 空白字符 |
| `\S` | `[^ \t\n\r\f\v]` | 非空白字符 |

```python
re.search(r"\d{3}-\d{4}-\d{4}", "电话: 010-1234-5678")
# 匹配中国座机号格式
```

---

## 四、捕获分组 `()` — 提取匹配的部分

```python
# 查找 "名字, 学院" 格式，分别提取
match = re.search(r"^(\w+), (\w+)$", "Harry, Gryffindor")
if match:
    print(match.group(0))   # "Harry, Gryffindor" — 完整匹配
    print(match.group(1))   # "Harry" — 第一个括号
    print(match.group(2))   # "Gryffindor" — 第二个括号
```

**要点**：
- `group(0)` = 整个匹配
- `group(n)` = 第 n 个括号的内容
- 括号从 1 开始编号

### 实战：解析 URL

```python
url = "https://cs50.harvard.edu/python/2022/weeks/9/"
match = re.search(r"https?://([^/]+)/(.+)", url)
if match:
    print(f"域名: {match.group(1)}")  # cs50.harvard.edu
    print(f"路径: {match.group(2)}")  # python/2022/weeks/9/
```

---

## 五、`re.sub()` — 查找并替换

```python
# 把"哈O大学"改成"哈佛大学"
text = "欢迎来到哈O大学学习Python"
result = re.sub(r"哈O大学", "哈佛大学", text)
# "欢迎来到哈佛大学学习Python"

# 用捕获组做格式转换
# 把 "Last, First" 变成 "First Last"
name = "Malan, David"
fixed = re.sub(r"^(\w+), (\w+)$", r"\2 \1", name)
print(fixed)  # "David Malan"
```

`re.sub(模式, 替换文本, 原文本)` — 替换文本里可以用 `\1` `\2` 引用捕获组。

---

## 六、常用 flags

```python
import re

# re.IGNORECASE — 忽略大小写
re.search(r"python", "PYTHON", re.IGNORECASE)  # 匹配！

# re.MULTILINE — ^$ 匹配每行的开头结尾
re.search(r"^#", "line1\n# comment", re.MULTILINE)
```

---

## 七、常见错误与陷阱

| 陷阱 | 说明 |
|------|------|
| **忘记 raw string** | `r"\d"` 正确，`"\d"` 可能被 Python 当成转义符 |
| **`search` vs `match`** | `search()` 在任意位置找；`match()` 只在开头匹配。一般用 `search` |
| **`*` vs `+`** | `*` = 0次或多次（可为空），`+` = 1次或多次（必须出现） |
| **`.` 不匹配换行** | 要匹配换行用 `re.DOTALL` flag |
| **分组编号混淆** | `group(1)` 是第一个 `(` `)`，不是第一个字符 |

---

## 与Java的对比

| 概念 | Java (`java.util.regex`) | Python (`re`) |
|------|--------------------------|---------------|
| 编译 | `Pattern.compile(r"\d+")` | `re.compile(r"\d+")`（可选） |
| 搜索 | `matcher.find()` | `re.search()` |
| 捕获组 | `matcher.group(1)` | `match.group(1)` |
| 替换 | `matcher.replaceAll("x")` | `re.sub(pattern, "x", text)` |
| 原始字符串 | 同 Python，也用 `r"..."` | `r"..."` |

---

## 你需要记住的正则速查

```
.     任意字符
*     0次或多次
+     1次或多次
?     0次或1次
^     开头
$     结尾
[]    字符集合
\d    数字
\w    单词字符
\s    空白
()    捕获组
|     或
```
