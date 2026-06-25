file_name = 'demo5.txt'
# 以写的方式打开文本文件，如文件存在则重写文件，否则创建新文件
with open(file_name , 'w' , encoding='utf-8') as file_obj:
# 追加，只允许在文件末尾追加数据，若文件不存在，则创建新文件
# with open(file_name , 'a' , encoding='utf-8') as file_obj:
    # write()来向文件中写入内容，
    # 如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
    # 该方法会可以分多次向文件中写入内容
    # 写入完成以后，该方法会返回写入的字符的个数
    file_obj.write('aaa\n')
    file_obj.write('bbb\n')
    file_obj.write('ccc\n')
    # file_obj.read()
    r = file_obj.write(str(123)+'123123')
    r = file_obj.write('今天天气真不错')
    print(r)
file_name = 'demo6.txt'
li_str=["i love java\n","i love python\n"]
with open(file_name , 'w' , encoding='utf-8') as file_obj:
    # writelines() 方法用于将字符串或字符串列表写入文件
    file_obj.writelines(li_str)

