
file_name = 'demo.txt'

# #关闭文件
# # 调用close()方法来关闭文件
# file_obj.close()

# with ... as 语句
# with open(file_name) as file_obj :
    # 在with语句中可以直接使用file_obj来做文件操作
    # 此时这个文件只能在with中使用，一旦with结束则文件会自动close()
    # print(file_obj.read())
try:
	with open(file_name) as file_obj :
		print(file_obj.read())   
except FileNotFoundError as e:
   print(file_name,'文件不存在~~',e)





