__author__ = '86131'
# 字符串的查找 find（）方法
string="Pythontn"
result=string.find('t')# 从第0个位置开始，查找在子串’t'在字符串”pypythontn"首次出现的位置
print(result)# 2
result=string.find('t',5)# 从第5个位置开始，查找在子串’t'在字符串”pypythontn"首次出现的位置
print(result)# 6
# 字符串的替换 replace()
# str.replace(old,new[,count] 返回替换后的新串
string="All things Are difficult before they Are easy Are good"
new_string=string.replace("Are","are")# 旧串中的"Are" 全部替换成"are"
print(new_string)# All things are difficult before they are easy are good
new_string=string.replace("Are","are",2)# 旧串中的"Are" 替换成"are" 替换2次
print(new_string)# All things are difficult before they are easy Are good
