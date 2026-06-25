__author__ = '86131'
# 求n!
# 边界条件 当n=1 时，所得的结果为1
# 递归公式 当n>1 时，所得的结果为 n*(n-1)!
def func(num):
    if num==1:
        return 1
    else:
        return num*func(num-1)
num=int(input("请输入一个整数："))
result=func(num)
print(f"{num}!=%d"%result)
