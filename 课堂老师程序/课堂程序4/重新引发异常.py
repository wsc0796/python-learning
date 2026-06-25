__author__ = '86131'
# 用任何不带任何参数的"raise"语句引发刚刚发生过的异常
def fn(a,b):
    try:
        if b==0:
            raise ZeroDivisionError("除数为零")
    except:
        raise
    c=a/b
    return c
try:
    print(fn(10,0))
except ZeroDivisionError as e:
    print(type(e))
    print(e)
