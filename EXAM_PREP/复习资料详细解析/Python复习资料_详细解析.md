# Python复习资料详细解析

> 来源：`python复习资料.docx` 与 `Python复习资料_参考答案.docx`。本文件按期末复习用途整理，重点是“为什么选这个答案”和“闭卷时怎么写”。

## 使用方法
1. 第一遍只看题目自己做。
2. 第二遍对答案，看解析里的“考点”。
3. 第三遍只背争议题、编程题模板和综合分析题。

## 易争议题提醒
- 单选 6：标准考试选 D，但 self 只是惯例名。
- 单选 18：题库把 bool 排除出数字类型，但 Python 中 bool 是 int 子类。
- 单选 20：题库按字典查找更快；若列表按下标访问也很快，题干不严谨。
- 单选 21：题库认为 B 错；Python 3 中该写法可作为仅限关键字参数。
- 单选 27：原题代码少右括号，按命题意图选 A。
- 单选 47：原资料缺题。
- 单选 104：A 和 D 都遍历键，题库预期 A。
- 综合 24：题目要求从字符串切出 rWo，单个普通切片做不到。

## 一、单项选择题详细解析
### 1. 答案：A
解析：标识符不能是关键字，不能以数字开头，不能包含 # 等非法字符；KeyWords 合法，with 是关键字，5var 和 _max#data 不合法。

### 2. 答案：D
解析：单引号、双引号、三引号都可以定义字符串，所以三种写法得到的都是 str。

### 3. 答案：B
解析：字符串下标从 0 开始，name[2:-1] 从第 2 位取到倒数第 1 位之前，结果为 thon programme。

### 4. 答案：C
解析：s.upper() 返回新字符串，不会原地修改 s；字符串不可变，所以 print(s) 仍输出 abc。

### 5. 答案：A
解析：range(0,10,3) 从 0 开始，每次加 3，不包含 10，得到 0、3、6、9。

### 6. 答案：D*
解析：题库预期考标准初始化方法 def __init__(self,a):。注意 self 是惯例名称，语法上也可写其他名字，但考试按 self 记。

### 7. 答案：D
解析：Python 支持多继承；GeneralManager 继承 Manager 的 salary。Director 的 __vote 是双下划线私有方法，会名称改写，不应直接当普通继承方法使用。

### 8. 答案：A
解析：面向对象以对象为中心组织程序，强调封装、继承、多态；不是某一种具体语言，也不只存在于设计阶段。

### 9. 答案：C
解析：r+ 表示读写方式打开；w 是只写且会覆盖，a 是追加，rw 不是标准模式。

### 10. 答案：D
解析：线程睡眠使用 time.sleep()；start 是启动线程，close/setDaemon 不是睡眠。

### 11. 答案：A
解析：format() 用于字符串格式化；join 是连接序列，split 是分割字符串，str 是类型转换。

### 12. 答案：B
解析：3*2 为 6，3**2 为 9，6>9 为 False；False is False 为 True，所以 x 为 True。

### 13. 答案：C
解析：'C'*2 得到 'CC'，'AB' + 'CC' 得到 'ABCC'。

### 14. 答案：D
解析：集合常见操作有并、交、差，对称差；没有“和”这种基本集合运算。

### 15. 答案：B
解析：表格有行和列，是典型二维数据组织方式。

### 16. 答案：B
解析：continue 跳过当前轮剩余语句，进入下一轮循环。break 是结束整个循环。

### 17. 答案：D
解析：变量名不能以数字开头；f中国、_a3、B_if 都合法。

### 18. 答案：D*
解析：题库通常将 bool 排除在数字类型外；严格说 bool 是 int 的子类。考试按题库选 D。

### 19. 答案：B
解析：0.0 和 0 的值相等，但类型不同：float 与 int。

### 20. 答案：B*
解析：题库预期字典查找更快，强调哈希查找；但若列表按下标访问，平均也是 O(1)，所以题干不严谨。

### 21. 答案：B*
解析：题库预期 *a 后面不能再有普通参数；但 Python 3 中 def vfunc(*a,b) 合法，b 是仅限关键字参数。按题库记 B。

### 22. 答案：C
解析：函数可以没有 return；没有 return 时默认返回 None。一个函数中也可以有多个 return 分支。

### 23. 答案：B
解析：切片赋值 l[1:3]='abc' 会把位置 1 到 2 替换成 'a','b','c'，新列表第 2 个索引处是 b。

### 24. 答案：D
解析：集合 set 无序且不支持下标索引，所以 del s[2] 会 TypeError。

### 25. 答案：B
解析：直接遍历字典默认遍历键，所以依次输出 a、c。

### 26. 答案：A
解析：Python 常见运行方式包括交互式解释器、命令行脚本、IDE；浏览器不是 Python 默认运行方式。

### 27. 答案：A*
解析：按命题意图分别输出 int、float、str；但原题最后一个 print 少右括号，真实运行会 SyntaxError。

### 28. 答案：C
解析：Python 3 已没有 long 类型，执行 long(10) 会 NameError。

### 29. 答案：C
解析：二进制 110100=52，八进制 101=65，十六进制 33=51，十进制 55=55，最大是 65。

### 30. 答案：D
解析：Python 单行注释用 #；三引号可作多行字符串/常被当多行注释用；// 不是 Python 注释。

### 31. 答案：D
解析：'1'.23 不是合法字符串字面量；其他都是字符串。

### 32. 答案：A
解析：range(110) 中能被 10 整除的 i 才累加：0+10+...+100=550。

### 33. 答案：A
解析：字符串也可以用三引号定义，因此“只可以使用单引号、双引号”错误。

### 34. 答案：B
解析：集合自动去重，{'a','b','b','a','c'} 为 3 个元素，再 add 已存在的 c，长度仍为 3。

### 35. 答案：D
解析：前三个参数接收 11、22、33，剩余 44、55 被 *args 收集成元组 (44,55)。

### 36. 答案：B
解析：readline() 读第一行字符串，包括换行符；list(data) 会把每个字符拆成列表元素。

### 37. 答案：B
解析：实例方法至少要接收实例对象参数，通常写 self；没有参数会导致对象调用时报参数数量错误。

### 38. 答案：C
解析：try 中出错后会转入 except，else 只在 try 无异常时执行。finally 一般仍会执行。

### 39. 答案：D
解析：global count 修改全局变量，count 变 6 后再加 2，输出 8。

### 40. 答案：B
解析：get(4,'小红') 找不到键 4 返回默认值小红；get(1) 返回键 1 对应的小明。

### 41. 答案：C
解析：jieba 支持中文分词，说“不支持”是错误的。

### 42. 答案：B
解析：li_one[:2] 为 [5,3]，sorted 后得到 [3,5]。

### 43. 答案：C
解析：a 是追加文本模式；二进制模式要加 b，如 rb、wb。

### 44. 答案：B
解析：Python 可用于 Web、科学计算、游戏、自动化等；操作系统内核级开发不是典型应用领域。

### 45. 答案：C
解析：name 不是 Python 关键字；if、is、and 都是关键字。

### 46. 答案：D
解析：同第 31 题，'1'.23 不是字符串。

### 47. 答案：原资料缺题
解析：参考答案说明原资料没有第 47 题，复习时直接跳过，不要自己脑补题干。

### 48. 答案：B
解析：转义字符由反斜杠 \ 开头，如 \n、\t。

### 49. 答案：B
解析：实例方法定义时通常必须有 self；类方法第一个参数通常是 cls。题干考实例方法不能无参数。

### 50. 答案：B
解析：列表 num_li 长度为 3，合法索引为 0、1、2，访问 3 会 IndexError。

### 51. 答案：A
解析：r 模式读文件，文件不存在会 FileNotFoundError；w/a 会创建文件，x 是排他创建。

### 52. 答案：B
解析：单元素元组必须有逗号：(1,)；(1) 只是整数 1。

### 53. 答案：D
解析：字符串可用三引号定义，多行字符串常用三引号。

### 54. 答案：B
解析：set('pypy123') 去重后为 p、y、1、2、3 共 5 个，再加 o，共 6 个。

### 55. 答案：A
解析：mkdir() 创建目录；rmdir 删除目录，getcwd 获取当前目录，chdir 切换目录。

### 56. 答案：B
解析：面向对象三大特性通常是封装、继承、多态；抽象不是这组三大特性的标准答案。

### 57. 答案：D
解析：except 应位于 try 后、else/finally 前；不能放在 else 和 finally 之后。

### 58. 答案：D
解析：li_one[:3] 是 [5,3,8]，降序 sorted 得 [8,5,3]。

### 59. 答案：C
解析：同第 43 题，a 是追加模式，不是二进制模式。

### 60. 答案：C
解析：方法内局部 count=20 输出 20；self.count +=20 会在实例上形成/修改 count，从类属性 21 得到 41。

### 61. 答案：C
解析：Python 注释符号是 #。

### 62. 答案：C
解析：定义函数使用 def。

### 63. 答案：B
解析：continue 结束本次循环并进入下一轮。

### 64. 答案：A
解析：实例方法第一个参数按惯例写 self。

### 65. 答案：A
解析：定义类使用 class。

### 66. 答案：A
解析：导入库并起别名的语法是 import numpy as np。

### 67. 答案：B
解析：元组下标从 0 开始，a[1] 是第二个元素 2。

### 68. 答案：B
解析：函数定义后不会自动执行，必须调用才执行。

### 69. 答案：C
解析：upper() 返回全大写字符串 PYTHON。

### 70. 答案：C
解析：集合元素无序且唯一，自动去重。

### 71. 答案：A
解析：成员运算符 in 判断 'a' 是否在 'abc' 中，结果 True。

### 72. 答案：B
解析：len('python') 为 6。

### 73. 答案：A
解析：s[2:5] 取索引 2、3、4，即 llo。

### 74. 答案：C
解析：_var 合法；变量名不能以数字开头，不能含减号，不能用关键字 class。

### 75. 答案：B
解析：3.14 是 float。

### 76. 答案：A
解析：if 分支一旦满足就执行，不再看 elif；x>3 成立输出 A。

### 77. 答案：A
解析：while 正常结束且没有 break，会执行 else，输出 0、1、2、Done。

### 78. 答案：B
解析：i=1 时 continue 跳过 print，所以只输出 0 和 2。

### 79. 答案：A
解析：[::-1] 表示反向切片，hello 变 olleh。

### 80. 答案：A
解析：split() 默认按空白分割，得到 ['a','b','c']。

### 81. 答案：A
解析：find('e') 返回字符 e 首次出现的下标 1。

### 82. 答案：A
解析：默认参数要放在非默认参数后，def func(a,b=1) 合法。

### 83. 答案：A
解析：*args 把多余位置参数收集为元组。

### 84. 答案：A
解析：**kwargs 把关键字参数收集为字典。

### 85. 答案：A
解析：open() 默认模式是 'r' 只读。

### 86. 答案：A
解析：json.loads() 将 JSON 字符串转为 Python 对象；dumps 是反向。

### 87. 答案：A
解析：Python 继承写法为 class Child(Parent):。

### 88. 答案：B
解析：子类 Dog 重写 speak，调用 d.speak() 优先执行子类方法。

### 89. 答案：A
解析：异常捕获结构是 try ... except ...。

### 90. 答案：A
解析：自定义异常通常继承 Exception。

### 91. 答案：A
解析：1/0 被 except 捕获输出 Error，finally 总会执行输出 Done。

### 92. 答案：D
解析：nonlocal 修改 outer 中的 x，第一次 f() 得 11，第二次在 11 基础上变 12。

### 93. 答案：B
解析：Python 是动态类型，同一个变量可先后引用不同类型对象。

### 94. 答案：A
解析：Python 没有独立 char 类型，单个字符也是字符串。

### 95. 答案：C
解析：% 是取余，5 除以 2 余 1。

### 96. 答案：D
解析：主动抛出异常用 raise。

### 97. 答案：A
解析：把字符串列表连接成字符串用 '分隔符'.join(list)。

### 98. 答案：C
解析：遍历 python，遇到 h 前输出 p、y、t，遇 h break。

### 99. 答案：C
解析：字符串不可变，因此“字符串是可变数据类型”错误。

### 100. 答案：A
解析：list('abc') 可把字符串拆成字符列表。

### 101. 答案：B
解析：len() 计算列表元素数量；count(x) 统计某个元素出现次数。

### 102. 答案：B
解析：捕获异常用 except。

### 103. 答案：A
解析：关键字参数/默认参数形式可写 b=1,a=2；其他选项存在默认参数顺序错误或不是函数头。

### 104. 答案：A*
解析：直接遍历字典得到键；D 中 item 也是键，但题库预期 A。若要键值对应使用 d.items()。

### 105. 答案：D
解析：CSV 本质是逗号分隔的表格文本。

## 二、填空题详细解析
### 1. 答案：`10`
解析：默认参数 b=10，调用 func(5) 只传 a，所以 b 保持默认值。

### 2. 答案：`{} 或 dict()`
解析：空字典可以直接写 {}，也可以调用 dict()。

### 3. 答案：`int()`
解析：int('123') 将数字字符串转换为整数。

### 4. 答案：`except`
解析：try 中出现异常后，由 except 捕获处理。

### 5. 答案：`print()`
解析：print 用于输出内容。

### 6. 答案：`False`
解析：True and False 只有两边都为 True 才为 True，所以结果 False。

### 7. 答案：`str()`
解析：str(123) 将整数转成字符串。

### 8. 答案：`return`
解析：函数通过 return 返回结果。

### 9. 答案：`input()`
解析：input 从键盘读取用户输入，返回字符串。

### 10. 答案：`and`
解析：逻辑与使用 and。

### 11. 答案：`0、1、2、3、4`
解析：range(5) 从 0 到 4，不包含 5。

### 12. 答案：`yth`
解析：'Python'[1:4] 取索引 1、2、3。

### 13. 答案：`[0, 2, 4]`
解析：range(3) 为 0、1、2，分别乘 2。

### 14. 答案：`lambda`
解析：lambda 用来定义匿名函数。

### 15. 答案：`global`
解析：函数内修改全局变量需要 global 声明。

### 16. 答案：`json`
解析：JSON 解析常用 json 模块。

### 17. 答案：`raise`
解析：raise 主动抛出异常。

### 18. 答案：`reverse()`
解析：list.reverse() 原地反转列表。

### 19. 答案：`sort()`
解析：list.sort() 原地排序列表。

### 20. 答案：`strip()`
解析：strip() 默认去除首尾空白。

### 21. 答案：`解释型`
解析：Python 通常归类为解释型语言。

### 22. 答案：`字节码 bytecode`
解析：Python 源码先编译为字节码，再由 PVM 执行。

### 23. 答案：`缩进`
解析：Python 用缩进表示代码块。

### 24. 答案：`import`
解析：导入模块使用 import。

### 25. 答案：`from 模块名 import *`
解析：该语句导入模块中公开名称，但不推荐滥用。

### 26. 答案：`elif`
解析：多分支结构为 if/elif/else。

### 27. 答案：`10`
解析：randint(1,10) 两端都包含。

### 28. 答案：`(1,)`
解析：单元素元组必须写逗号。

### 29. 答案：`self`
解析：实例方法第一个参数通常是 self。

### 30. 答案：`匿名函数`
解析：lambda 定义的函数叫匿名函数。

### 31. 答案：`都等价为 False`
解析：空列表和 None 在条件判断中都为假。

### 32. 答案：`赋值/定义`
解析：变量第一次使用前要先赋值。

### 33. 答案：`def`
解析：函数定义以 def 开始。

### 34. 答案：`print()`
解析：基本输出函数是 print。

### 35. 答案：`缩进`
解析：Python 依靠缩进划分语句块。

### 36. 答案：`列表`
解析：常见序列类型：字符串、列表、元组。

### 37. 答案：`join()`
解析：大量字符串连接优先用 join，效率高。

### 38. 答案：`%`
解析：% 既可求余，也可做旧式字符串格式化。

### 39. 答案：`continue`
解析：continue 跳过本轮，继续下一轮。

### 40. 答案：`3`
解析：UTF-8 中常见汉字占 3 个字节。

### 41. 答案：`2`
解析：a+=b 等价于 a=a+b，即 5+(-3)=2。

### 42. 答案：`type()`
解析：type 查看对象类型。

### 43. 答案：`切片`
解析：列表元素可通过索引或切片访问。

### 44. 答案：`列表`
解析：readlines() 返回由每行字符串组成的列表。

### 45. 答案：`双下划线 __`
解析：类成员名前加 __ 会触发名称改写，形成私有效果。

### 46. 答案：`Exception`
解析：自定义异常通常继承 Exception。

### 47. 答案：`Python 源代码 .py`
解析：模块本质上通常是一个 .py 文件。

### 48. 答案：`for`
解析：for 循环也叫遍历循环。

### 49. 答案：`全局变量`
解析：global 将函数内名字声明为全局变量。

### 50. 答案：`close()`
解析：文件使用完应 close；更推荐 with open 自动关闭。

### 51. 答案：`super()`
解析：子类调用父类方法常用 super()。

### 52. 答案：`切片 list[:] 或 copy()`
解析：浅复制列表常用切片或 copy。

### 53. 答案：`rstrip()`
解析：rstrip 去掉右侧/尾部空白。

### 54. 答案：`items()`
解析：dict.items() 返回键值对视图。

### 55. 答案：`seek()`
解析：seek(offset) 控制文件读写位置。

### 56. 答案：`AssertionError`
解析：assert 条件为假会抛出 AssertionError。

### 附加. 答案：`None`
解析：'' 为假，or 返回右侧 None，所以 result 是 None。

## 三、判断题详细解析
### 1. 答案：√
解析：strip 默认删除字符串两端空白。

### 2. 答案：×
解析：字典键唯一，重复键会覆盖旧值。

### 3. 答案：×
解析：位置参数依赖顺序。

### 4. 答案：×
解析：if 可以嵌套。

### 5. 答案：×
解析：字符串可以包含转义字符。

### 6. 答案：×
解析：字典按键访问，不按位置索引。

### 7. 答案：×
解析：变量有作用域限制。

### 8. 答案：√
解析：子类可以重写父类方法。

### 9. 答案：√
解析：elif 必须跟在 if 后，不能单独出现。

### 10. 答案：×
解析：for 可以遍历字符串。

### 11. 答案：√
解析：集合可使用 copy 做浅拷贝。

### 12. 答案：√
解析：即使异常未被当前 except 捕获，finally 通常也先执行。

### 13. 答案：×
解析：continue 只跳过当前一轮，不结束所有循环。

### 14. 答案：√
解析：format 使用 {} 占位。

### 15. 答案：×
解析：类方法既可类调用，也可实例调用。

### 16. 答案：×
解析：实例方法也可通过类名显式传入对象调用。

### 17. 答案：×
解析：random 是标准库模块，使用前仍要 import。

### 18. 答案：√
解析：两种导入都能导入内容，但 from import * 不推荐。

### 19. 答案：√
解析：Python 区分大小写。

### 20. 答案：×
解析：元组不可变。

### 21. 答案：×
解析：time 使用前要 import。

### 22. 答案：√
解析：函数可以嵌套定义。

### 23. 答案：×
解析：集合不支持索引。

### 24. 答案：√*
解析：题库按三引号可作多行注释判对；严格说它是字符串字面量。

### 25. 答案：√
解析：Python 通常归为解释型语言。

### 26. 答案：×
解析：字典仍然按键访问。

### 27. 答案：×
解析：集合和字典是可变且不可哈希，不能作为集合元素。

### 28. 答案：√
解析：元组和列表都支持下标访问。

### 29. 答案：√
解析：字符串不可变。

### 30. 答案：√
解析：列表元素可以是列表。

### 31. 答案：×
解析：Python 没有 ++ 运算符。

### 32. 答案：×
解析：默认参数、*args、**kwargs 会改变实参数量要求。

### 33. 答案：√*
解析：题库按字典无序判对；现代 Python 保持插入顺序。

### 34. 答案：√*
解析：while 语法必须有条件；条件恒真会死循环。

### 35. 答案：×
解析：类属性和类方法可通过类访问。

### 36. 答案：√
解析：Python 变量名支持 Unicode，包括中文。

### 37. 答案：√
解析：链式比较等价于 and 连接。

### 38. 答案：√
解析：字符串不可变。

### 39. 答案：√
解析：集合可以浅拷贝。

### 40. 答案：×
解析：字符串不能直接和整数相加。

### 41. 答案：√
解析：列表 + 表示拼接。

### 42. 答案：√
解析：集合比较只看元素，不看顺序。

### 43. 答案：√
解析：多返回值本质是元组打包。

### 44. 答案：√
解析：非默认参数必须在默认参数前。

### 45. 答案：√
解析：with open 退出代码块自动关闭文件。

### 46. 答案：√
解析：__name 会触发名称改写。

### 47. 答案：√
解析：try 后至少要有 except 或 finally。

### 48. 答案：√
解析：raise 可主动抛异常。

### 49. 答案：×
解析：Exception 捕获不了所有 BaseException，例如 KeyboardInterrupt。

### 50. 答案：√*
解析：通常 finally 会执行，除非进程被强制终止等极端情况。

### 51. 答案：√
解析：装饰器可扩展函数功能。

### 52. 答案：×
解析：*args 和 **kwargs 可以单独使用。

## 四、综合分析题详细解析

### 1. 九九乘法表补空
答案：`for j in range(1, i + 1):`

解析：外层 `i` 控制乘法表的行数，第 `i` 行应该从 `1*i` 打印到 `i*i`，所以内层 `j` 的范围是 `1` 到 `i`。`range(1, i + 1)` 右边不包含，因此要写 `i + 1`。

### 2. 世界杯随机分组
答案：`random.randint`；`countrys.pop(index)`。

解析：每次从剩余国家列表中随机抽一个下标，`pop(index)` 会取出该元素并从列表删除，避免同一国家重复分组。

### 3. 列表引用与 clear
答案一：使用 `list1.clear()` 后输出 9 个空列表。
答案二：改成 `list1 = []` 后，list2 中保留每次 append 时引用的旧列表内容。

解析：`list2.append(list1)` 保存的是列表对象的引用。`clear()` 会把同一个列表对象清空，所以所有引用都看到空列表；`list1 = []` 是让变量指向新列表，不会清空旧对象。

### 4. lambda 排序
答案：`[('a', 6), (5, 7), ('c', 12), ('b', 'A')]`

解析：排序键是每个元组第 2 个元素。若是字符串，用 `ord()` 转成 ASCII；`'A'` 的 ASCII 是 65，因此排在数字 6、7、12 后。

### 5. 字符串切片与 for-else
答案：`fb ef`

解析：`s[::-1]` 得到反转字符串。`for...else` 中只要没有 break，循环自然结束后会执行 else。题目难点是负步长 range 和 for-else 的执行时机。

### 6. 字典按值降序
答案：`[('c', 8), ('d', 7), ('e', 5), ('a', 4), ('b', 2)]`

解析：`dict.items()` 得到键值对，`key=lambda x:x[1]` 按值排序，`reverse=True` 降序。

### 7. readline 转列表
答案：`['7', '6', '5', '4', '3', '2', '1', '\n']`

解析：`readline()` 读一行字符串并保留换行符；`list(data)` 会把字符串拆成单个字符。

### 8. MyDate 补空
答案：
```python
def __init__(self, y, m, d)
MyDate.__months[2] = 29
assert 1 <= m <= 12, "无效月份"
```
运行 `MyDate(2020,13,33)` 输出：`无效月份`。

解析：构造方法用于初始化年月日；闰年 2 月有 29 天；`assert` 条件不满足时抛出 AssertionError，异常信息就是第二个参数字符串。

### 9. CSV 文本读写补空
答案：
```python
ls.append(line.split(","))
csv_out = open("score_out.csv", "w")
csv_out.write(",".join(line) + "\n")
```
解析：CSV 的本质是逗号分隔文本，读入时 split，写出时 join，并手动补换行。

### 10. 类属性列表输出
答案：`['roll over', 'play dead']`

解析：`tricks = []` 是类属性，所有实例共享同一个列表。两个对象添加的 trick 都进入同一列表。

### 11. *args 与 **kwargs
答案：`1 2 3 (4,) {'e': 5}`

解析：a、b、c 分别接收 1、2、3；多余位置参数 4 进入 args；关键字参数 e=5 进入 kwargs 字典。

### 12. 递归阶乘
答案：`120`

解析：`factorial(5)=5*4*3*2*1`，当 n==0 时返回 1 作为递归出口。

### 13. 字典浅拷贝
答案：
```python
{1: 'one', 2: 'two'}
{1: 'ONE', 2: 'two'}
```
解析：字典外层被复制，修改 b[1] 不影响 a。

### 14. 列表直接赋值
答案：
```python
[1, 5, 3]
[1, 5, 3]
```
解析：`b = a` 不是复制，而是两个变量指向同一个列表。

### 15. filter 补空
答案：`lambda`

解析：`filter(lambda i: i > 10, li)` 保留大于 10 的元素。

### 16. 多返回值拆包
答案：`age`

解析：函数返回三个值，实际是元组，按位置拆给 name、age、city。

### 17. 构造方法属性赋值
答案：`name`

解析：`self.name = name` 把形参保存为实例属性。

### 18. f-string 补空
答案：`name`、`age`

解析：f-string 中 `{变量名}` 会替换为变量值。

### 19. 文件对象读取
答案：`f`

解析：`with open(...) as f` 中 f 是文件对象，调用 `f.read()`。

### 20. JSON 序列化与反序列化
答案：`dumps`、`loads`

解析：`json.dumps()` 把字典转 JSON 字符串；`json.loads()` 把 JSON 字符串转回字典。

### 21. 列表前三个元素
答案：`:3`

解析：`numbers[:3]` 从开头取到索引 3 之前，即前三个。

### 22. **kwargs 遍历
答案：`kwargs.items()`

解析：遍历字典键值对要用 `.items()`。

### 23. 类属性与实例属性访问
答案：`MyClass`、`obj`。注意原题 `obj = MyClass()` 缺 name 实参，应改为 `obj = MyClass("Alice")`。

解析：类属性可通过类名访问，实例属性通过对象访问。

### 24. 输出 rWo 的切片题
答案：严格说单个普通切片无法从 `Hello, World!` 得到 `rWo`。可写：`text[9] + text[7:9]`；若题目本意是 `Wor`，应写 `text[7:10]`。

解析：这是题库错误题，考试时看老师是否修正题干。

### 25. 筛选偶数
答案：`x % 2 == 0`

解析：偶数能被 2 整除，余数为 0。

### 26. __str__ 补空
答案：`self.name`

解析：`__str__` 返回对象的可读字符串，访问实例属性用 self.name。

### 27. 二进制读取模式
答案：`rb`

解析：图片是二进制文件，应使用 rb 读取。

### 28. nonlocal 输出
答案：
```text
33
22
33
```
解析：inner2 中 `nonlocal b` 修改的是 inner1 作用域中的 b；不影响 func 里的 b=11。

### 29. 默认参数输出
答案：
```text
Hello, Alice!
Good morning, Bob!
```
解析：第一次使用默认 msg，第二次显式传入覆盖默认值。

### 30. 自定义异常输出
答案：`捕获到错误: 自定义错误`

解析：MyError 继承 Exception，可被对应 except 捕获。

### 31. strip / upper / replace
答案：
```text
Python编程
␠␠PYTHON编程␠␠
␠␠Java编程␠␠
```
解析：strip 去掉首尾空格；upper 返回大写新字符串；replace 返回替换后的新字符串，原字符串不变。

### 32. 字典转列表并排序
答案：先按字典插入顺序打印键值，再输出按分数升序的二维列表，最后输出最大分对应的名字 `bush`。

解析：`items()` 得到键值对；追加 `[分数, 名字]` 后，列表排序默认先比较第 0 项分数。

### 33. 浅拷贝与深拷贝
答案：
```text
Original: [['a', 2, 3], [4, 5, 6]]
Shallow copy: [['a', 2, 3], [4, 5, 6]]
Deep copy: [[1, 2, 3], [4, 5, 6]]
```
解析：浅拷贝复制外层列表，但内层列表共享；深拷贝连内层对象也复制。
## 五、编程题详细解析

### 1. Student / SoftwareStudent 模块题
考点：类、构造方法、私有属性、继承、super、模块导入。

关键写法：
```python
# mysystem.py
class Student:
    def __init__(self, sid, dormitory):
        self._sid = sid              # 可被继承/约定受保护
        self.__dormitory = dormitory # 私有属性

    def get_sid(self):
        return self._sid

    def get_dormitory(self):
        return self.__dormitory

    def set_dormitory(self, dormitory):
        self.__dormitory = dormitory

class SoftwareStudent(Student):
    def __init__(self, sid, dormitory, studio):
        super().__init__(sid, dormitory)
        self.studio = studio

    def get_studio(self):
        return self.studio
```

解析：`_sid` 是约定受保护，子类可用；`__dormitory` 会名称改写，子类不能直接访问。子类构造方法必须先用 `super().__init__()` 初始化父类部分。

### 2. 1 到 100 偶数和
考点：range、循环累加。
```python
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
```
解析：步长为 2，直接遍历偶数，结果为 2550。也可以遍历 1 到 100，用 `if number % 2 == 0` 判断。

### 3. 随机生成 128 个英文字母并写文件
考点：random、string、with open。
```python
import random
import string

letters = "".join(random.choices(string.ascii_letters, k=128))
with open("letter.txt", "w", encoding="utf-8") as file:
    file.write(letters)
```
解析：`string.ascii_letters` 包含大小写英文字母；`random.choices(..., k=128)` 是有放回抽样；写文本文件用 w。

### 4. 统计字符出现次数
考点：字典计数。
```python
text = input("请输入字符串：")
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)
```
解析：`dict.get(key, 0)` 表示如果没有这个字符，就从 0 开始计数。

### 5. 二进制文件拷贝
考点：rb、wb。
```python
with open("source.png", "rb") as source:
    data = source.read()
with open("target.png", "wb") as target:
    target.write(data)
```
解析：图片、音频、压缩包等都应按二进制处理。

### 6. 性能监控装饰器
考点：装饰器、闭包、*args、**kwargs、返回值透传。
```python
import time
from functools import wraps

def monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时：{(end - start) * 1000:.3f} ms")
        return result
    return wrapper
```
解析：装饰器本质是“接收函数，返回新函数”。必须 `return result`，否则原函数返回值会丢失。

### 7. 记录函数调用次数
考点：nonlocal、闭包。
```python
def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"第 {count} 次调用")
        return func(*args, **kwargs)
    return wrapper
```
解析：`count` 在外层函数中，wrapper 要修改它，必须使用 `nonlocal`。

### 8. User / Admin 用户权限模型
考点：父类、子类、继承方法、新增属性。
```python
# mysystem.py
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

class Admin(User):
    def __init__(self, name, password, authority):
        super().__init__(name, password)
        self.authority = authority

    def get_authority(self):
        return self.authority
```
解析：Admin 是 User，所以继承 User；管理员多出 authority，所以在子类中新增属性。

### 9. 删除列表中的 .txt 文件名
考点：列表遍历删除风险、copy、列表推导式。
```python
files = ["a.txt", "b.py", "c.txt", "image.png"]
for filename in files.copy():
    if filename.endswith(".txt"):
        files.remove(filename)
print(files)
```
更推荐：
```python
files = [filename for filename in files if not filename.endswith(".txt")]
```
解析：遍历原列表时删除元素可能跳项，所以要遍历副本或用新列表接收。

### 10. 记录函数名、参数、返回值的装饰器
考点：装饰器、参数收集、返回值。
```python
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"函数名：{func.__name__}")
        print(f"位置参数：{args}")
        print(f"关键字参数：{kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper
```
解析：`*args` 接收位置参数，`**kwargs` 接收关键字参数；调用原函数后保存 result，打印后再返回。
## 六、最后优先背熟
- 类与继承：`__init__`、`self`、私有属性、`super()`。
- 文件：`with open`、`r/w/a/rb/wb`、`read/readline/readlines`、`write`。
- 异常：`try/except/else/finally`、`raise`、自定义异常继承 `Exception`。
- 函数：默认参数、`*args`、`**kwargs`、`lambda`、`nonlocal/global`。
- 数据结构：列表赋值 vs 浅拷贝 vs 深拷贝，字典 `items()`，集合无序去重。
