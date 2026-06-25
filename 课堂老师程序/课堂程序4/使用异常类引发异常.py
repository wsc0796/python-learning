__author__ = '86131'
# 使用异常类引发异常 该方式会隐式创建一个该异常类型的对象并抛出
try:
    password=input("请输入密码")
    if len(password)<=6:
        raise Exception  #抛出Exception异常类对象
except Exception as e:
    print(type(e))
    print("密码长度小于6")

