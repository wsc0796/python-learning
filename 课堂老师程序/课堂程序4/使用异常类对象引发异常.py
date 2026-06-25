__author__ = '86131'
# 使用异常类对象(使用有参的构造方法）引发异常
try:
    password=input("请输入密码")
    if len(password)<=6:
        raise Exception("密码长度小于6")
except Exception as e:
    print(e)
