__author__ = '86131'
# 函数是组织好的，实现特点功能的代码段
def fn():
    pass
def add(): # 定义一个无参函数
    result=11+22
    print(result)
def add_modify(a,b): # 定义一个有参函数
    result=a+b
    return result
print(add,type(add))
add()#调用一个无参函数 33
x=add
x()
print(add_modify(10,20))#调用一个有参函数 30

