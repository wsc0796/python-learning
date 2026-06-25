file_name = 'aa.FLAC' # 二进制文件
# file_name = 'demo3.txt' # 文本文件
# 读取模式
# t 读取文本文件（默认值）
# b 读取二进制文件
# 以读的方式打开二进制文件
with open(file_name , 'rb') as file_obj:
# with open(file_name , 'rt',encoding='utf-8') as file_obj:
    # 读取文本文件时，size是以字符为单位的
    # 读取二进制文件时，size是以字节为单位
    # print(file_obj.read(100))
    # 将读取到的内容写出来
    # 定义一个新的文件
    # new_name = 'demo13.txt'
    new_name = 'bb.FLAC'
    # 以写的方式打开二进制文件
    with open(new_name , 'wb') as new_obj:
        # 定义每次读取的大小
        chunk =100*1024
        while True :
            # 从已有的对象file_obj文件中读取数据
            content = file_obj.read(chunk)
            # 内容读取完毕，终止循环
            if not content :
                break
            # 将读取到的数据写入到new_obj所指新对象文件中
            new_obj.write(content)