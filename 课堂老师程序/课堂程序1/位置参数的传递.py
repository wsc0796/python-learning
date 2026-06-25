__author__ = '86131'
# 函数被调用时，会将实参按照相应的位置依次传递给形参
def get_max(a,b): #定义函数
    if a>b:
        print(a,"是较大的值")
    else:
        print(b,"是较大的值")
get_max(8,5) #调用函数
# 8 是较大的值