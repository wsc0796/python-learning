__author__ = '86131'
# nonlocal关键字可以在局部作用域中修改嵌套作用域中声明的变量
def test(a):
    number=10
    def test_in():
        nonlocal number
        number+=20
        print(number,a)
    test_in()
    print(number)

test(15) # 30

