__author__ = '86131'
# 在 Python中使用raise语句可以显示的抛出异常
# 1.使用异常类引发异常 该方式会隐式创建一个该异常类型的对象并抛出
# raise IndexError
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/使用raise语句抛出异常.py", line 4, in <module>
    raise IndexError
IndexError
'''
# 2.使用异常类对象(使用无参的构造方法）引发异常
# raise IndexError()
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/使用raise语句抛出异常.py", line 12, in <module>
    raise IndexError()
IndexError
'''
# 2.使用异常类对象(使用有参的构造方法）引发异常
# raise IndexError('索引下标超出范围')
'''
raceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/使用raise语句抛出异常.py", line 20, in <module>
    raise IndexError('索引下标超出范围')
IndexError: 索引下标超出范围
'''
# 3 重新引发（抛出）异常
# 使用任何不带任何参数的"raise"语句引发刚刚发生过的异常
try:
    raise  IndexError('索引下标超出范围')
except:
    raise  # eccept 子句后的代码又使用raise 语句抛出刚刚发生的异常
'''
Traceback (most recent call last):
  File "D:/pythonProjects/Dirstjsd/ppyp/使用raise语句抛出异常.py", line 30, in <module>
    raise  IndexError('索引下标超出范围')
IndexError: 索引下标超出范围
'''