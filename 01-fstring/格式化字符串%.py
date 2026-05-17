__author__ = '86131'
# 1.使用%格式化字符串
# format % values
# format 标识一个字符串 包含单个或多个 真实数据占位的格式符如 %S,%d,%f
# % 代表格式化操作
# values 代表单个或多个真实数据 多个数据以元组形式存储
name='张三'
age=27
ave=88.856
address='北京昌平区'
print("姓名：%s"% name)
print("年龄：%6d岁\n家庭住址：%s\n平均成绩%.2f"% (age,address,ave))

