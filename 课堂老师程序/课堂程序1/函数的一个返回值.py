__author__ = '86131'
# 函数中的return语句会在函数调用结束时将数据返回给程序，让程序回到函数被调用的位置继续执行
# 定义一个敏感词过滤函数
def filter_sensitive_words(words):#定义函数
    if "山寨"in words: #如果语句中含有山寨
        new_words=words.replace("山寨","*")# 把山寨替换为“*”
    return new_words #返回替换后的字符串
result=filter_sensitive_words("这个手机是山寨版的吧！")
print(result)# 这个手机是*版的吧！