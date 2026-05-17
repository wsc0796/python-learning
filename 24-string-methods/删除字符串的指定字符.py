__author__ = '86131'
old_string='  Life is short,Use Python!    '
strip_str=old_string.strip() # 删除字符串头部和尾部的空格
print(f'strip方法:{strip_str}显示')# strip方法:Life is short,Use Python!显示
lstrip_str=old_string.lstrip()# 删除字符串的头部字符
print(f'lstrip方法:{lstrip_str}显示')# lstrip方法:Life is short,Use Python!    显示
rstrip_str=old_string.rstrip()# 删除字符串的尾部字符
print(f'rstrip方法:{rstrip_str}显示')# rstrip方法:  Life is short,Use Python!显示