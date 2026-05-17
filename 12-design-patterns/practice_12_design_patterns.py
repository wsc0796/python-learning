"""
12 — 设计模式练习
Python 特有的简洁实现，对照你的 Java 知识。
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ============================================================
# 练习1：工厂模式 — 创建不同的存储后端
# ============================================================
# TODO: 用字典实现工厂模式
# 定义 LocalStorage 和 CloudStorage，都有 save(data) 方法
# factory = {"local": LocalStorage, "cloud": CloudStorage}
# create_storage(type) → 返回对应实例

class LocalStorage:
    def save(self, data: str):
        print(f"[本地] 保存: {data}")

class CloudStorage:
    def save(self, data: str):
        print(f"[云端] 保存: {data}")

# 你的代码...
# storage_factory = ...
# def create_storage(storage_type: str) -> ???:
#     ...

# 验证
# local = create_storage("local")
# cloud = create_storage("cloud")
# local.save("测试")    # [本地] 保存: 测试
# cloud.save("测试")    # [云端] 保存: 测试


# ============================================================
# 练习2：策略模式 — 排序策略
# ============================================================
# TODO: 用函数（而不是类）实现策略模式

def asc_sort(data: list[int]) -> list[int]:
    """正序"""
    return sorted(data)

def desc_sort(data: list[int]) -> list[int]:
    """倒序"""
    return sorted(data, reverse=True)

# TODO: 实现 Sorter 类，接收策略函数
class Sorter:
    # 你的代码...
    pass

# 验证
# sorter = Sorter(desc_sort)
# print(sorter.sort([3, 1, 4, 1, 5]))   # [5, 4, 3, 1, 1]


# ============================================================
# 练习3：观察者模式 — 事件系统
# ============================================================
# TODO: 实现一个简单的事件系统
# on(event_name, callback) → 注册监听
# emit(event_name, data) → 触发事件

class EventBus:
    # 你的代码...
    pass

# 验证
# bus = EventBus()
# bus.on("user_login", lambda user: print(f"日志: {user} 登录"))
# bus.on("user_login", lambda user: print(f"通知: 欢迎 {user}"))
# bus.emit("user_login", "张三")
# 期望输出两行


# ============================================================
# 练习4：单例模式
# ============================================================
# TODO: 用 __new__ 实现 Logger 单例
# 所有 Logger() 创建的都是同一个实例

class Logger:
    _instance = None

    def __new__(cls):
        # 你的代码...
        pass

    def log(self, msg: str):
        print(f"[LOG] {msg}")

# 验证
# l1 = Logger()
# l2 = Logger()
# print(l1 is l2)   # True
# l1.log("测试")


# ============================================================
# 练习5：破坏实验
# ============================================================
# 如果不小心把 EventBus 的 listeners 设置成类变量（而不是实例变量）
# 会有什么问题？

class BuggyEventBus:
    listeners = []  # 类变量！

    def on(self, callback):
        BuggyEventBus.listeners.append(callback)

    def emit(self, data):
        for cb in BuggyEventBus.listeners:
            cb(data)

# 取消注释，看看为什么 Buggy 了：
# b1 = BuggyEventBus()
# b2 = BuggyEventBus()
# b1.on(lambda d: print(f"b1: {d}"))
# b2.on(lambda d: print(f"b2: {d}"))
# b1.emit("测试")
# 输出几行？为什么？


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 设计模式练习完成！")
