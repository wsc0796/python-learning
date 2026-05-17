__author__ = '86131'
# 格式 f-string 语法 f"{变量名}
# 以f引领字符串 在字符串使用{变量名}
age=20
ave_score=88.8534
gender='男'
print(f"年龄：{age},性别：{gender},平均成绩：{ave_score:.2f}")  # 平均成绩 以浮点数形式输出保留2位小数
