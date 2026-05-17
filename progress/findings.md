# 学习发现

| 日期 | 发现 | 关联 |
|------|------|------|
| 2026-05-06 | 类型提示 `: type` 和 `-> type` 是可选的，Python 不检查 | Java 强制类型声明 |
| 2026-05-06 | `字符串 * N` 重复字符串 | Java 没有，需循环 |
| 2026-05-06 | 列表推导式 `[x for x in list if cond]` 压缩 for+if+append | Java Stream `.filter().toList()` |
| 2026-05-06 | `.items()` 遍历 dict = Java `.entrySet()` | 但 Python 能直接拆 key, value |
| 2026-05-06 | 对象调方法：`obj.method()`，不写 `method.obj()` | 和 Java 一样 |
| 2026-05-06 | f-string `f"Hello, {name}"` = Java `String.format()` | 更简洁 |
| 2026-05-07 | 字符串三种引号 + 转义：单/双引号等价，三引号跨行 | Java 只有双引号，15+才有文本块 |
| 2026-05-07 | Python 格式化三代演进：`%` → `.format()` → f-string | Java 基本只用 `String.format()` |
| 2026-05-07 | `find()` = Java `indexOf()`，找不到返回 -1；`index()` 会抛异常 | 用 find 更安全 |
| 2026-05-07 | `replace(old, new, count)` count 限替换次数 | Java 无直接等价 |
| 2026-05-07 | `split()` 支持 `split(sep, maxsplit)` 限制分割次数 | 和 Java 一致 |
| 2026-05-07 | `join()` 方向：`"-".join(list)` 不是 `list.join("-")` | 和 Java `String.join("-", list)` 相反 |
| 2026-05-07 | `title()` 每词首字母大写，`capitalize()` 仅句首 | Java 两个都要手写 |
| 2026-05-07 | `strip/lstrip/rstrip` 是去空白三件套 | Java 只有 trim（仅两端） |
| 2026-05-07 | `center/ljust/rjust` 内置对齐填充 | Java 需手写或 `String.format()` |
| 2026-05-07 | dict 键必须加引号 `emp["age"]`，不加引号去找同名变量 | Java `map.get("key")` 同理 |
| 2026-05-07 | Python 从上到下执行，`def` 必须写在调用之前 | Java 方法顺序无所谓 |
| 2026-05-07 | 函数重名时后面覆盖前面，但调用在旧定义之后仍执行旧版 | 和 Java 方法重载不同 |

## 错误日志

| 现象 | 我的猜测 | 真实原因 | 下次怎么更快定位 |
|------|---------|---------|----------------|
| 类里定义 `info()` 却调用 `s.introduce()` | 以为方法名自动匹配 | 方法名写错，Python 只认精确名字 | 写完方法名 → 调用时看一眼定义处的名字 |
| 把 `s = Student(...)` / `print(...)` 缩进在 class 里面 | 以为和 Java 一样写在类里就行 | Python class 里只能放 def 方法，执行代码必须顶格写在外面 | class 缩进完了按 Tab 退出来，再写执行代码 |
| `append.fruits("葡萄")` | 不知道方法调用顺序 | Python 是 `对象.方法()` | 谁调方法，谁在前面 |
| 以为 `-> int` 必须写 | 以为是语法强制 | 类型提示可选，去掉也能跑 | 先忽略，不写 |
| `emp[age]` 报 NameError | 以为 dict 键和变量一样写 | dict 键是字符串必须加引号 `emp["age"]` | Java 的 `map.get("key")` 也要引号，一样 |
| `result.append(employees)` 加了整个列表 | 参数名和循环变量搞混 | `employees` 是整个入参列表，`emp` 是当前元素 | 写完 for 循环确认一下变量名是谁 |
| `get_adults()` 返回 None | 以为重名函数自动覆盖 | 函数定义在调用后面 + 旧 `pass` 版本在调用前面 | Python 从上到下执行，def 必须写在调用之前 |
| BankAccount 创建对象代码写在类里面 | — | class 里面只能放 def 方法，不能写执行代码 | 写完 class 缩进退出来，再写 `acct = ...` |
| 创建对象传 2 个参数但 `__init__` 需要 3 个 | 以为少传也行 | 参数数量必须严格对应 | 数一下 `__init__` 有几个参数（含 self 不算），传几个 |
| `get_balance` 里判断 `if _balance>0` 才返回 | 以为余额 <=0 就不能查 | 查询余额就是返回数值，不判断正负 | getter 只 return，不做业务判断 |
| `_balance` 初始化为 `0.0` 没用传入的 `balance` | 忘了用参数 | 初始化必须用传进来的值 | 检查 `__init__` 里每个属性是否用了对应参数 |

## 学校材料补充（2026-05-07 运算符+流程控制）

| 文件来源 | 新增内容 | 整合到 |
|----------|---------|--------|
| 标识符和关键字.py | 35关键字+命名规范（蛇形/驼峰） | theory.md §命名规范 |
| 数字类型.py | 进制表示、浮点范围、bool真值表 | theory.md §数字类型补充 |
| 赋值运算符.py | 海象运算符 `:=` + 多重赋值 | theory.md §赋值运算符 |
| 算数运算符.py | `/` vs `//` + 混合运算 | theory.md §算术运算符 |
| 逻辑运算符.py | 短路求值 + 非布尔值and/or | theory.md §逻辑运算符 |
| 比较运算符.py | 链式比较 `a < b < c` | theory.md §比较运算符 |
| 成员运算符.py | `in` / `not in` | theory.md §成员运算符 |
| 位运算符.py | `<<` / `>>` | theory.md §位运算符 |
| 运算符的优先级.py | 优先级表 | theory.md §运算符优先级 |
| while语句.py | while循环 | theory.md §while |
| 跳转语句.py | break/continue | theory.md §break/continue |
| 循环嵌套.py | 双重循环 | theory.md §循环嵌套 |
| if语句.py | input() 函数 | theory.md §input() |

## 待完成（含新增）

- ✅ 字符串模块已完整整合到 references/python-strings.md（7大模块，9个源文件）
- TODO 4.1 get_adults() 函数 — 未写
- TODO 5.1 lambda + 列表推导式 — 未写
- TODO 6.1 装饰器填空题 — 未写
- 🆕 TODO 7.1 while 循环求和 — 未写
- 🆕 TODO 7.2 链式比较 — 未写
- 🆕 TODO 7.3 break 练习 — 未写
- 🆕 TODO 7.4 短路求值填空 — 未写
