__author__ = '86131'
def fn(filename):
    try:
        file=None
        with open(filename,'r',encoding='utf_8') as file:
            print(file.read())
    except Exception as error:
        print(error)
    finally:  # 无论是否产生异常都会执行
        if file!=None :
            file.close()
        print("文件已经关闭")
fn("file123.txt")

