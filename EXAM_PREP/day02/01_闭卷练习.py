"""
Day 2 闭卷练习：字符串与组合数据类型。
"""
from unittest import result


# 题 1（考点：字符串切片，建议 5 分钟）
# 输出 text 的前三个字符、最后两个字符、倒序字符串。
def task01(text: str) -> None:

    print(text[0:3])
    print(text[-2:])
    print(text[::-1])


# 题 2（考点：字符串方法，建议 6 分钟）
# 把句子 sentence 中的空格分割成单词列表，再用 "-" 拼接。
def task02(sentence: str) -> None:
    words = sentence.split()
    result = "-".join(words)
    print(result)

# 题 3（考点：列表，建议 8 分钟）
# 给列表 nums 添加 100，删除第一个 0，按升序排序后输出。
def task03(nums: list[int]) -> None:
    nums.append(100)
    nums.remove(0)
    nums.sort()
    print(nums)

# 题 4（考点：元组，建议 5 分钟）
# 给定 point=(x,y)，输出 x 和 y 的和。
def task04(point: tuple[int, int]) -> None:
     result =point[0]+point[1]
     print(result)

# 题 5（考点：字典，建议 8 分钟）
# 统计字符串 text 中每个字符出现次数。
# 使用count方法，思路：
# 先遍历字符串的全部内容，在循环的同时使用count方法
#正确版：先把字典的重复字符去重，再遍历。再使用count方法
def task05(text: str) -> None:
    result ={}
    for index in set(text):
        result[index] =text .count(index)
    print(result)
#准备一个空字典 result
#遍历 text 里的每一个字符
#如果这个字符还没统计过
#就把它作为 key，出现次数作为 value 放进字典
#最后打印字典

# 题 6（考点：集合，建议 6 分钟）
# 输出 nums 去重后的结果和去重后数量。
#去重：set,求数量：len
def task06(nums: list[int]) -> None:
    result=set(nums)
    print(result)
    print(len(result))
# 题 7（考点：推导式，建议 8 分钟）
# 用列表推导式生成 1 到 n 中所有偶数的平方。
#先判断n是否为偶数,再循环输出为偶数的平方，即n**n(当n为偶数时)

def task07(n: int) -> None:
    X =[]
    for i in range(n+1):
        if(n%2==0):
            X.append(i**2)
    print(X)
    X =[i**2 for i in range(n+1) if n%2==0 ]
    print(X)
# 综合题（考点：列表+字典，建议 18 分钟）
# 给定学生成绩列表 [{"name": "A", "score": 80}, ...]，
# 输出最高分学生姓名、平均分、及格人数。
#我的思路是先用sort函数来把成绩从大到小排序，再让输出第一个，但是平均分、及格人数我不知道怎么搞
def task08(students: list[dict]) -> None:
    # 1. 最高分学生
    top = max(students, key=lambda s: s["score"])
    print(top["name"])

    # 2. 平均分
    total = sum(s["score"] for s in students)
    avg = total / len(students)
    print(avg)

    # 3. 及格人数（>= 60）
    passed = 0
    for s in students:
        if s["score"] >= 60:
            passed += 1
    print(passed)


if __name__ == "__main__":
    print("Day 2: 请逐个调用 task01-task08 自测。")
    task01("abcde")
    task02("hello   world")
    task08([{"name": "A", "score": 80}, {"name": "B", "score": 55}, {"name": "C", "score": 90}])

