__author__ = '86131'
class Cat():# 定义父类 默认继承基类object 相当于class Cat(object)
    def __init__(self,color):
        self.color=color
    def walk(self):
        print("走猫步")
class ScottishFold(Cat): # 定义子类（折耳猫）继承父类（猫）
    pass
print(type(ScottishFold))
flod=ScottishFold("灰色") # 创建子类对象 调用父类的构造方法__init__(self,color)
print(f"{flod.color}的折耳猫")# 子类访问从父类继承的属性 灰色的折耳猫
flod.walk() # 子类访问从父类继承的方法 走猫步

# 运行说明：1.创建子类对象 要调用有参的构造方法 现从子类找如果没有找到在从父类找
# 增加子类对象属性 并附初值。2.在执行子类对象的walk()方法时，若当前子类对象没有
# 就去子类 类对象找 如没有就去父类 类对象找


