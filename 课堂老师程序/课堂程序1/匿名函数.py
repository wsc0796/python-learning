__author__ = '86131'
# 匿名函数是一类无需定义标识符的函数
# Python 中使用lambda关键字定义匿名函数
# 定义好的匿名函数不能直接使用，最好使用一个变量保存函数地址 以便调用
# 语法：lambda 参数列表 : 返回值(表达式）
temp=lambda a,b:a+b # 定义匿名函数 并把函数对象的地址交给temp变量保存
print(type(temp))# <class 'function'>
print(temp(10,20))# 30

def temp(a,b):
    return a+b
print(temp(10,20)) #30