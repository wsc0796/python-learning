__author__ = '86131'
# 函数在定义时 可以在内部嵌套定义另一个函数
# 函数外部无法直接调用内层函数，只能在外层函数中调用内层函数
def add_modify(a,b): # 定义外层函数
    result=a+b
    print(result)
    def test():      # 定义内层函数
        print("我是内层函数")
    test() #外层函数中调用内层函数
add_modify(10,20)# 30 函数外部只能调用外层函数
