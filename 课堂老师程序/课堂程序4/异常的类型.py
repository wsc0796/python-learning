__author__ = '86131'
'''
Python的BaseException是所有异常类的基类
Exception是所有内置的，非系统退出的异常的基类
Exception类内置了众多常见异常
'''
# 1.NameError:是程序中使用了未定义的变量时引发的异常
# print(test)
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 8, in <module>
    print(test)
NameError: name 'test' is not defined
'''
# 2.IndexError:是程序越界访问时引发的异常
# new_list=[]  # 定义一个空列表
# print(new_list[0])
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 17, in <module>
    print(new_list[0])
IndexError: list index out of range
'''
# 3.AttributeError 是对象访问不存在的属性引发异常
class Car:
    pass
car=Car()
car.color="黑色"
car.brand="五菱"
# print(car.color)
# print(car.brand)
# print(car.name)
'''
黑色
五菱
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 32, in <module>
    print(car.name)
AttributeError: 'Car' object has no attribute 'name'
'''
# 4.FileNotFoundError:未找的指定文件或目录
# file=open("text.txt")
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 41, in <module>
    file=open("text.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
'''
# 5.ZeroDivisionError异常：数字相除，除数为零
# number=10.6/0.0
'''Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 49, in <module>
    number=10.6/0.0
ZeroDivisionError: float division by zero
'''
# 6.ValueError：非数值异常
# num=int(input("请输入整数"))
'''
请输入整数10a
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/异常的类型.py", line 56, in <module>
    num=int(input("请输入整数"))
ValueError: invalid literal for int() with base 10: '10a'
'''