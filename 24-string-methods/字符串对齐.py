__author__ = '86131'
sentence='hello world'
center_str=sentence.center(13,'-')# 长度为13，居中显示 使用-补齐
print(center_str)# -hello world-
ljust_str=sentence.ljust(13,'*')# 长度为13，左对齐 使用*补齐
print(ljust_str)# hello world**
rjust_str=sentence.rjust(13,'%')# 长度为13，右对齐 使用%补齐
print(rjust_str)# %%hello world