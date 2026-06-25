file_name = 'demo2.txt'
# 以读的方式打开文本文件（默认）
with open(file_name , encoding='utf-8') as file_obj:
    # read() 若设置为-1或未提供 则一次读取文件中所有数据
    print(file_obj.read())
print("*******")
with open(file_name , encoding='utf-8') as file_obj:
    # readline() 该方法可以用来读取一行内容
    print(file_obj.readline())
print("*******")
with open(file_name , encoding='utf-8') as file_obj:
    # readlines() 该方法可以用来读取文件中所有数据, 返回一个列表，文件中每一行对应列表每一个元素
    print(file_obj.readlines())

print("*******")
with open(file_name , encoding='utf-8') as file_obj:
    # 该方法可以从file_obj所指的文件中读取一行内容给t,然后输
    # 出，再读取下一行内容给t，然后输出，直到文件结束。
    for t in file_obj:
        print(t,end='')

    