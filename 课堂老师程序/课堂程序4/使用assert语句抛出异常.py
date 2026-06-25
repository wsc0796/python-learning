__author__ = '86131'
# assert 后跟着一个表达式和一个字符串（异常信息）
# assert 表达式[,异常信息]
# 当表达式为False时 使用异常信息调用有参的构造方法创建
# AssertionError异常对象AssertionError（异常信息）并抛出
try:
    num_one=int(input("请输入被除数"))
    num_two=int(input("请输入除数"))
    assert  num_two!=0 ,'除数不能为0'
    print("结果为：",num_one/num_two)
except Exception as e:
    print(type(e))
    print(e)
