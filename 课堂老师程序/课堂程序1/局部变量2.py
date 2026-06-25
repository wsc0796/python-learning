__author__ = '86131'
# 不同函数内部可以包含同名的局部变量，它们相互独立互不影响
def test_one():
    number=10 # 定义局部变量
    print(number) #函数内部访问局部变量
def test_two():
    number=20 # 定义局部变量
    print(number) #函数内部访问局部变量
test_one()# 10
test_two()# 20
