__author__ = '86131'
try:
    num_one=int(input("请输入被除数"))
    num_two=int(input("请输入除数"))
    print("结果为：",num_one/num_two)
except Exception as error:  # error 获取异常对象
    print("出错了，原因：",error)
print("程序执行结束")