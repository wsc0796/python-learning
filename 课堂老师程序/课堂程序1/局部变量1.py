__author__ = '86131'
# 局部变量指在函数内部定义的变量，它只能在函数内部被使用，

def test_one():
    number=10 # 定义局部变量
    print(number) #函数内部访问局部变量
test_one()
# print(number) #函数外部不能访问局部变量