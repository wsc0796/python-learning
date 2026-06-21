"""
Day 1 改错题。

要求：先在注释里写出错误原因，再修改代码。
为保证本文件可运行，错误代码放在字符串里。
"""


# 题 1（考点：if 语法，建议 5 分钟）

score = 80
if score >= 60:
    print("及格")

# 少了：

# 题 2（考点：类型转换，建议 5 分钟）

a = int( input("a="))
b = int( input("b="))
print(a + b)  # 目标：输出两个数字的和



# 题 3（考点：range 边界，建议 6 分钟）

# 目标：输出 1 到 10
for i in range(1, 11):
    print(i)



if __name__ == "__main__":
    print("Day 1 改错题：请把每段 bug 复制到临时区域修复。")

