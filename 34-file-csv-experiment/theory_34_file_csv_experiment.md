# 34 - 文件拷贝与 CSV 实验（超详细版）

这章只为完成老师这份实验：

1. 图片拷贝
2. 文件备份
3. 文件内容大小写互换
4. CSV 学生成绩录入、求总分、按姓名查找

你现在不要想着“一口气写完整程序”。先按下面 5 关走。

```text
txt 拷贝
-> 图片拷贝
-> 文件备份
-> 大小写互换
-> CSV 成绩
```

## 0. 先理解：程序操作文件到底在干嘛

你平时手动操作文件是这样：

```text
双击文件 -> 看到内容 -> 复制内容 -> 新建文件 -> 粘贴进去 -> 保存
```

Python 做的事情一样，只是换成代码：

```text
open 打开文件
read 读取内容
write 写入内容
close 关闭文件
```

Python 推荐写法是：

```python
with open("文件名", "模式", encoding="utf-8") as f:
    ...
```

你可以先把它理解成：

```text
with open(...) as f:
    在这里操作文件
```

`f` 就是“文件遥控器”。你通过 `f.read()` 读取，通过 `f.write()` 写入。

## 1. 第一关：txt 文件拷贝

目标：

```text
把 source.txt 的内容复制到 source_copy.txt
```

人工做法：

```text
打开 source.txt
复制里面全部文字
新建 source_copy.txt
把文字粘贴进去
保存
```

Python 做法：

```python
with open("source.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("source_copy.txt", "w", encoding="utf-8") as f:
    f.write(content)
```

逐行解释：

```python
with open("source.txt", "r", encoding="utf-8") as f:
```

意思是：

```text
打开 source.txt
用 r 模式，也就是 read，读取
用 utf-8 编码，避免中文乱码
把这个打开的文件临时叫做 f
```

```python
content = f.read()
```

意思是：

```text
把文件里的全部内容读出来
放进变量 content
```

```python
with open("source_copy.txt", "w", encoding="utf-8") as f:
```

意思是：

```text
打开 source_copy.txt
用 w 模式，也就是 write，写入
如果文件不存在，就创建
如果文件已存在，就覆盖旧内容
```

```python
f.write(content)
```

意思是：

```text
把 content 里的文字写进新文件
```

你先只要记住这个模板：

```python
# 读
with open(源文件, "r", encoding="utf-8") as f:
    content = f.read()

# 写
with open(目标文件, "w", encoding="utf-8") as f:
    f.write(content)
```

## 2. 第二关：图片拷贝

图片和 txt 不一样。

txt 是文字，人能直接看懂：

```text
hello python
```

图片在电脑里其实是一堆二进制数据，人直接看不懂：

```text
10001001 01010000 01001110 ...
```

所以图片不能用：

```python
"r"
"w"
encoding="utf-8"
```

图片要用：

```python
"rb"  # read binary，读二进制
"wb"  # write binary，写二进制
```

模板：

```python
with open("old.png", "rb") as f:
    data = f.read()

with open("new.png", "wb") as f:
    f.write(data)
```

逐行解释：

```python
data = f.read()
```

这里读出来的不再是普通字符串，而是二进制数据。

注意：

```python
with open("old.png", "rb") as f:
```

这里没有 `encoding="utf-8"`。

因为：

```text
encoding 只给文本文件用
图片 / 视频 / 压缩包 不写 encoding
```

## 3. 第三关：文件备份

文件备份其实也是“复制文件”。

比如：

```text
need_backup.txt
```

备份成：

```text
need_backup_backup.txt
```

你可以手动读写，但 Python 已经提供了工具：`shutil`。

```python
import shutil

shutil.copy2("need_backup.txt", "need_backup_backup.txt")
```

这行代码的意思是：

```text
把第一个文件复制成第二个文件
```

为什么叫 `copy2()`？

你现在不用深究。先记住：

```text
普通文件备份，用 shutil.copy2()
```

## 4. 第四关：大小写互换

老师题目是：

```text
将文件中所有的小写字母转换成大写字母，
将所有的大写字母转换成小写字母
```

比如：

```text
Hello Python
```

变成：

```text
hELLO pYTHON
```

这个不是单纯全大写，也不是单纯全小写。

三个方法区别：

```python
"Hello".upper()      # "HELLO"
"Hello".lower()      # "hello"
"Hello".swapcase()   # "hELLO"
```

所以这题最合适的是：

```python
text.swapcase()
```

完整流程：

```text
读原文件
把内容 swapcase
写到新文件
```

代码模板：

```python
with open("case_source.txt", "r", encoding="utf-8") as f:
    text = f.read()

result = text.swapcase()

with open("case_result.txt", "w", encoding="utf-8") as f:
    f.write(result)
```

## 5. 第五关：CSV 成绩文件

CSV 文件可以理解成“用逗号分隔的表格”。

老师给的格式：

```text
姓名,语文,数学,英语,理综
tom,124,137,145,260
jack,116,143,139,263
```

它看起来像文本，其实表示一张表：

| 姓名 | 语文 | 数学 | 英语 | 理综 |
|------|------|------|------|------|
| tom | 124 | 137 | 145 | 260 |
| jack | 116 | 143 | 139 | 263 |

Python 操作 CSV 要先导入：

```python
import csv
```

### 5.1 写入 CSV

模板：

```python
with open("students.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "语文", "数学", "英语", "理综"])
    writer.writerow(["tom", 124, 137, 145, 260])
    writer.writerow(["jack", 116, 143, 139, 263])
```

逐行解释：

```python
writer = csv.writer(f)
```

意思是：

```text
创建一个 CSV 写入工具
以后用 writer 往文件里写一行一行的数据
```

```python
writer.writerow([...])
```

意思是：

```text
写入一行
列表里的每个元素就是一列
```

为什么写：

```python
newline=""
```

先记住：

```text
写 CSV 时固定加 newline=""
否则 Windows 上可能多出空行
```

为什么写：

```python
encoding="utf-8-sig"
```

先记住：

```text
CSV 里有中文，并且可能用 Excel 打开，就用 utf-8-sig
```

### 5.2 读取 CSV

模板：

```python
with open("students.csv", "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

读出来的每一行是一个列表：

```python
["tom", "124", "137", "145", "260"]
```

注意：从 CSV 读出来的分数是字符串，不是整数。

所以计算前要：

```python
score = int("124")
```

### 5.3 计算总分

一行数据：

```python
row = ["tom", "124", "137", "145", "260"]
```

每个位置含义：

```text
row[0] = 姓名
row[1] = 语文
row[2] = 数学
row[3] = 英语
row[4] = 理综
```

计算总分：

```python
total = int(row[1]) + int(row[2]) + int(row[3]) + int(row[4])
```

把总分加到这一行后面：

```python
new_row = row + [total]
```

例如：

```python
["tom", "124", "137", "145", "260", 666]
```

### 5.4 按姓名查找

核心逻辑：

```text
输入一个姓名
一行一行读 CSV
如果这一行的第 0 列等于输入姓名
就打印这一行所有信息
```

代码思路：

```python
name = input("请输入姓名：").strip()

for row in reader:
    if row[0] == name:
        print(row)
```

## 最后：你今天只做第一关

不要一上来写 CSV。

今天只做：

```text
copy_text_file()
```

也就是：

```text
读 source.txt
写 source_copy.txt
运行程序
看到第一关从“未完成”变成“OK”
```

你看到：

```text
OK: txt 拷贝 -> source_copy.txt
```

就算今天成功。

## 备考相关

- [[EXAM_PREP/day05/00_今日任务]] — Day 5 文件与异常
- [[EXAM_PREP/day06/00_今日任务]] — Day 6 老师课堂代码重放（CSV 读写）
- [[EXAM_PREP/day07/00_今日任务]] — Day 7 学生管理系统综合题

