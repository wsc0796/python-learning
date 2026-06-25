file_name = 'demo2.txt'
try:
    with open(file_name,encoding='utf-8') as file_obj:
       # content = file_obj.read(-1)
        content = file_obj.read(5)# 一次读取5个字符
        print(content)
        print(len(content))
except FileNotFoundError :
    print(file_name,' 这个文件不存在！')

# 读取大文件的方式
file_name = 'demo.txt'
try:
    with open(file_name) as file_obj:
        # 定义一个变量，来保存文件的内容
        file_content = ''
        # 定义一个变量，来指定每次读取的大小
        chunk = 100
        # 创建一个循环来读取文件内容
        while True:
            # 读取chunk大小的内容
            content = file_obj.read(chunk)

            # 检查是否读取到了内容
            if not content:
                # 内容读取完毕，退出循环
                break

            # 输出内容
            # print(content,end='')
            file_content += content

except FileNotFoundError :
    print(file_name,'这个文件不存在！')


print(file_content)