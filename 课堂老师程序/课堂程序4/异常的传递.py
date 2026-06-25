__author__ = '86131'
# 如果程序中异常没有处理，默认情况下会将该异常传递到上一级（调用它的方法），
# 如果上一级仍然没有处理异常，那么就会继续向上传递，直到异常被处理或程序崩溃
def get_width():                 # 计算边长
    print("get_width开始执行")
    num=int(input("请输入除数："))
    width_len=10/num
    print("get_width执行结束")
    return width_len
def calc_area():                 # 计算正方形面积
    print("calc_area开始执行")
    with_len=get_width()
    print("calc_area执行结束")
    return with_len*with_len
def show_area():                # 输出正方形面积
    try:
        print("show_area开始执行")
        area_val=calc_area()
        print(f"正方形的面积为：{area_val}")
        print("show_area执行结束")
    except ZeroDivisionError as e:
        print(f"捕获到异常:{e}")
show_area()
'''
show_area开始执行
calc_area开始执行
get_width开始执行
请输入除数：0
捕获到异常:division by zero
'''