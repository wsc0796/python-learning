__author__ = '86131'
# python的return语句可以返回多个值 这些值将被保存到元组中
def move(x,y,step): #定义函数
    nx=x+step
    ny=y-step
    return nx,ny # 使用return返回多个值
a,b=move(100,100,60)# 把多个返回值依次传给变量a,b
print(a,b)# 160 40
result=move(100,100,60)# 把多个返回值传给元组result
print(type(result))# <class 'tuple'>
print(result)# (160, 40)


