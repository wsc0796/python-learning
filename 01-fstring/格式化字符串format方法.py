__author__ = '86131'
# format()方法语法如下
# str.format（values）
# str 表示要被格式的字符串 包含一个或多个真实数据占位符{}
# values 表示一个或多个待替换的真实数据
name='张三'
age=27
address='北京昌平区'
print("姓名：{}".format(name))
# 顺序格式化
print("年龄：{}岁\n家庭住址：{}".format (age,address))
# 编号格式化
print("姓名：{1}\n年龄：{0}".format (age,name))
# 名称格式化
print("姓名：{name1}\n年龄：{age1}".format (name1=name,age1=age))
# 指定浮点型数据精度
point=19
total=22
print('所占百分比：{:.2%}'.format(point/total))  # 保留2位小数
print("%.2f"%(point/total))
print(f"{point/total:.2f}")