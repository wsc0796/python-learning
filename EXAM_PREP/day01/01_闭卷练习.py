"""
Day 1 闭卷练习：基础语法与流程控制。

要求：不要翻答案，先把 pass 替换成自己的代码。
运行：python EXAM_PREP/day01/01_闭卷练习.py
"""


# 题 1（考点：类型转换，建议 5 分钟）
# 输入两个字符串数字 a、b，转成整数后输出它们的和、差、积。
def task01(a: str, b: str) -> None:
    print( int(a) + int(b) )
    print( int(a) - int(b) )
    print( int(a) * int(b) )

# 题 2（考点：运算符，建议 5 分钟）
# 给定整数 n，输出 n 除以 3 的商和余数。
def task02(m:int) -> None:
    A =m%3
    B =m//3
    print(A,B)












def task02(n: int ) -> None:
     a =n%3
     b =n//3
     print(a,b)

# 题 3（考点：if，建议 6 分钟）
# 根据 score 输出：>=90 优秀，>=60 及格，否则 不及格。
def task03(score: int) -> None:
    if score >= 90:
        print("优秀")
    elif  score >= 60:
        print("及格")
    else:
        print("不及格")

# 题 4（考点：for/range，建议 8 分钟）
# 输出 1 到 n 之间所有偶数的和。
def task04(n: int) -> None:
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    print(total)


# 题 5（考点：while，建议 8 分钟）
# 用 while 计算 1+2+...+n。
def task05(n: int) -> None:
    total =0
    i =1
    while i <= n:
        total += i
        i += 1

    print(total)


# 题 6（考点：break/continue，建议 8 分钟）
# 遍历 1 到 n：跳过 3 的倍数；遇到大于 20 的数停止；输出剩余数字。
def task06(n: int) -> None:
    for n in range(1,n+1):
        if n > 20:
            break


        if n % 3 == 0:
                continue
        print(n)


# 题 7（考点：循环 else，建议 8 分钟）
# 判断 n 是否为素数。用 for...else 写。
def task07(n: int) -> None:
    if n < 2:
        print(f"{n} 不是素数")
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} 不是素数")
            break
    else:
        print(f"{n} 是素数")




# 综合题：输入 3 次成绩，统计最高分、最低分、平均分和不及格人数

def task08(scores: list[int]) -> None:
    highest = scores[0]
    lowest = scores[0]
    total = 0
    fail_count = 0

    for score in scores:
        total += score

        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

        if score < 60:
            fail_count += 1

    average = total / len(scores)

    print(f"最高分：{highest}")
    print(f"最低分：{lowest}")
    print(f"平均分：{average:.2f}")
    print(f"不及格人数：{fail_count}")


# 输入部分
scores = []

for i in range(3):
    score = int(input(f"请输入第{i + 1}个学生的成绩："))
    scores.append(score)

task08(scores)

def task09() -> None:
    c="hello"
    for ch in c:  # h e l l o
        print(ch)
    for item in [1, 2, 3]:  # 1 2 3
        print(item)
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i*j}", end="\t")
        print()  # 换行
if __name__ == "__main__":
    print("Day 1: 请逐个调用 task01-task08 自测。")
task01("12", "5")
task02(17)
task03(59)
task03(95)
task04(10)
task05(100)
task06(25)
task09()