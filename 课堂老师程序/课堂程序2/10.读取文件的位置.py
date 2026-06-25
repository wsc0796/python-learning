#以二进制方式打开文本文件
with open('demo.txt','rb') as file_obj:
    # seek() 可以修改当前读取的位置-从第6个位置开始读取
    file_obj.seek(6)# b'ipsum dolor sit amet, consectetur...其中b表示字节字符串
#     # seek()需要两个参数
#     #   第一个 是要切换到的位置
#     #   第二个 计算位置方式
#     #       可选值：
#     #           0 从头计算，默认值
#     #           1 从当前位置计算
#     #           2 从最后位置开始计算
    print(file_obj.read())
    # tell() 方法用来查看当前读取的位置
    print('当前读取到了 -->',file_obj.tell())
    # 以文本方式打开文本文件
with open('demo2.txt','rt' , encoding='utf-8') as file_obj:
    print(file_obj.read(9))  # 读取9个字符
    print("*******")
    # seek() 可以修改当前读取的位置 按字节 一个汉字3字节
    file_obj.seek(9)
    print(file_obj.read())

    # tell() 方法用来查看当前读取的位置
    print('当前读取到了 -->',file_obj.tell())