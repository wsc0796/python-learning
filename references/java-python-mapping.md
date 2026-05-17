# Java → Python 对照表

核心思想：**你不是在学新语言，是在用另一种语法表达已会的逻辑。**

## 基础语法

| Java | Python | 说明 |
|------|--------|------|
| `int x = 1;` | `x = 1` | 动态类型，不需要声明类型 |
| `String name = "张三";` | `name: str = "张三"` | 类型提示（可选，运行时忽略） |
| `List<String> list = new ArrayList<>()` | `list = ["a", "b"]` | 列表直接量，无需 new |
| `list.add("c")` | `list.append("c")` | 尾部添加 |
| `list.get(0)` | `list[0]` | 索引访问 |
| `list.subList(1, 3)` | `list[1:3]` | 切片（Python 特色，更强大） |
| `Map<String, Object> map = new HashMap<>()` | `d = {"k": "v"}` | 字典直接量 |
| `map.put("k", "v")` | `d["k"] = "v"` | 添加键值 |
| `map.get("k")` | `d.get("k")` | 取值 |
| `map.getOrDefault("k", "def")` | `d.get("k", "def")` | 带默认值取值 |
| `for (String s : list)` | `for s in list:` | for-each 遍历 |
| `for (int i = 0; i < n; i++)` | `for i in range(n):` | 索引遍历 |
| `for (Map.Entry<K,V> e : map.entrySet())` | `for k, v in d.items():` | map 遍历 |
| `if (x > 0) { ... }` | `if x > 0:` | 无括号，用缩进表示代码块 |
| `public ReturnType method(params)` | `def method(params) -> ReturnType:` | 函数定义 |
| `// 单行注释` | `# 单行注释` | 注释符号不同 |
| `/* 多行 */` | `""" 多行 """` | 多行注释/文档字 |
| `true / false / null` | `True / False / None` | 布尔/空值（大写！） |

## 面向对象

| Java | Python | 说明 |
|------|--------|------|
| `class Employee { }` | `class Employee:` | 类定义 |
| `this.name` | `self.name` | self = this，但必须显式写在参数里 |
| `public Employee(name) { }` | `def __init__(self, name):` | 构造 |
| `extends` | `(ParentClass)` | 继承：`class Dog(Animal):` |
| `@Override` | 无需注解 | 方法覆盖自动生效 |
| `interface` | 无关键字 | Python 用抽象基类（ABC）或鸭子类型 |

## 框架对比（FastAPI → Spring Boot）

详见 `fastapi-spring-mapping.md`

## 常见陷阱

| 陷阱 | 错误写法 | 正确写法 |
|------|---------|---------|
| 变量名冲突 | `list = [1,2,3]` 后不能再用 `list()` | 不要用内置类型名做变量 |
| 可变默认参数 | `def f(lst=[])` 多次调用共享同一个 list | `def f(lst=None)` + 内部判断 |
| 深拷贝 vs 浅拷贝 | `b = a`（引用复制） | `b = a.copy()`（list）或 `import copy; b = copy.deepcopy(a)` |
| 字符串不可变 | `s[0] = 'a'`（报错） | `s = 'a' + s[1:]` |
