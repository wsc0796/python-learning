__author__ = '86131'
# 在函数内部 可以使用global关键字将局部变量声明为全局变量
# 这样便可以在函数内部修改全局变量
number=10 # 定义全局变量
def test_one():
    global number # 使用global声明变量number为全局变量
    number+=1
    print(number) #函数内部访问全局变量
test_one()# 11
print(number) #函数外部访问全局变量 11
