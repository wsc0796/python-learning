__author__ = '86131'
def func(a,b,/,c):# / 指明前面的参数a,b均为仅限位置参数 后面不要求
    print(a,b,c)

func (10,20,30)
func (10,20,c=30)
# func(a=10,b=20,c=30) #出错
