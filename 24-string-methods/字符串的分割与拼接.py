__author__ = '86131'
# 用split()方法进行字符串分割
string_example="The more efforts you make,the more fortune you get"
# ['The', 'more', 'efforts', 'you', 'make,the', 'more', 'fortune', 'you', 'get']
print(string_example.split())# 默认分隔符为空格’’
# ['The ', 'ore efforts you ', 'ake,the ', 'ore fortune you get']
print(string_example.split('m'))# 以字母m为分隔符
# ['Th', ' mor', ' efforts you make,the more fortune you get']
print(string_example.split('e',2))# 以字母e为分隔符,并分隔2次
# 1.用join()方法 使用指定的字符串连接字符串并生成一个新的字符串
# 使用 * 连接字符串’Python'中的各个字符生成新字符串
symbol='*'
world='Python'
print(symbol.join(world))# P*y*t*h*o*n
# 用'+'拼接字符串
star='Py'
end='thon'
print(star+end)# Python