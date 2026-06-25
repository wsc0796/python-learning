__author__ = '86131'
import time
# 希望在不修改原函数的情况下，来对函数进行扩展
def begin_end(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前计算开始时间，执行后计算结束时间
       参数：
            old 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*args , **kwargs):
        print('开始执行~~~~')
        time_begin=time.time()
        # 调用被扩展的函数
        result = old(*args , **kwargs)  # sub(10,20)
        time_end=time.time()
        print('执行结束~~~~')
        print(f"函数{old.__name__}执行时间为{(time_end-time_begin)*1000:.2f}毫秒")# 精确到毫秒 保留2位小数
        # 返回函数的执行结果
        return result
    # 返回新函数
    return new_function
# 目标函数
def sub(a,b):
    print("函数正在执行")
    time.sleep(1)
    return a-b
# print(sub(10,20))
f2 = begin_end(sub)
result=f2(10,20)
print(result)
print("*******************************")
@begin_end
def add(a,b):
    print("函数正在执行")
    time.sleep(2)
    return a+b
result=add(3,2)
print(result)
