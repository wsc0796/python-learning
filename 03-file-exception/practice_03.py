"""
Day 3 练习：文件读写 + 异常处理
读完 theory 后，手敲每个 TODO。
运行：python practice_03.py
"""

# ============================================================
# 第一组：文件写入（必做）
# ============================================================

# TODO 1：用 "w" 模式创建文件 test_output.txt，写入三行任意内容
# 注意：encoding="utf-8"
# 在这里写：

with open("test_output.txt","w",encoding="utf-8") as f:
    f.write("hello world\n")
    f.write("test_output.txt\n")
    f.write("nice to meet you\n")

# TODO 2：用 "a" 模式追加一行
# 然后去文件夹打开 test_output.txt，对比 "w" 和 "a" 的区别
# 在这里写：
with open("test_output.txt","a",encoding="utf-8") as f:
    f.write("增加的一行\n")



# ============================================================
# 第二组：文件读取（必做）
# ============================================================

# TODO 3：用 read() 全部读出来，打印
# 在这里写：
print("逐行读:")
with open("test_output.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line)

# TODO 4：用 readlines() 读，打印它的类型和内容
# 在这里写：
with open("test_output.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    print(f"readlines()类型：{type(lines)}")
    print(f"readlines() 内容：{lines}")
# TODO 5：用 for line in f 逐行读，用 strip() 去换行符
# 在这里写：
with open("test_output.txt","r",encoding="utf-8")as f:
    for line in f:
        print(line.strip())

# ============================================================
# 第三组：异常处理（必做）
# ============================================================

# TODO 6：用 try/except 包一个 input(int())，输入非数字时不崩溃
# 提示：捕获 ValueError
# 在这里写：

try:
     age = int(input("输入年龄："))
     print(f"明年你{age+1}岁")
except ValueError:
     print("请输入数字！")

# TODO 7：一个 try 配两个 except，分别捕获 ValueError 和 ZeroDivisionError
# 用户输入两个数字做除法
# 在这里写：
try:
      a = int(input("被除数："))
      b = int(input("除数："))
      print(f"{a} ÷ {b} = {a / b}")
except ValueError:
      print("请输入数字！")
except ZeroDivisionError:
      print("除数不能为0！")

# ============================================================
# 第四组：文件 + 异常组合（必做）
# ============================================================

# TODO 8：打开一个不存在的文件，用 FileNotFoundError 捕获
# 在这里写：
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在，请检查路径")

# TODO 9：读文件 config.txt，不存在则创建它并写入默认内容
# 在这里写：
try:
      with open("config.txt", "r", encoding="utf-8") as f:
          print(f.read())
except FileNotFoundError:
      with open("config.txt", "w", encoding="utf-8") as f:
          f.write("# 默认配置\n")
          f.write("host = localhost\n")
          f.write("port = 8080\n")
      print("config.txt 不存在，已创建默认配置文件")

print("\n=== Day 3 全部完成！===")
