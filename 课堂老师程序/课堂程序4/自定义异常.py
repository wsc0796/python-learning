__author__ = '86131'
# 自定义异常类需要继承Exception类或其子类
class ShortInputError(Exception):
    '''自定义异常类'''
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast
try:
    text=input("请输入密码:")
    if len(text)<3 :
        raise ShortInputError(len(text),3)
except ShortInputError as e:
    print("ShortInputError:输入的长度是%d,长度至少应该是%d"%(e.length,e.atleast))
else:
    print("密码设置成功")
print("程序执行结束")