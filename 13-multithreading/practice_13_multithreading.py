"""
13 — 多线程练习
注意：Python 多线程适合 I/O 密集型，不适合 CPU 计算密集。
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import threading
import time
from concurrent.futures import ThreadPoolExecutor


# ============================================================
# 练习1：创建并启动线程
# ============================================================
# TODO: 补全代码，创建 3 个线程同时执行 task 函数
# 每个线程打印 "线程 {name} 工作中..."
# 主线程等待所有子线程结束

def task(name: str):
    for i in range(3):
        print(f"线程 {name}: 第{i+1}次")
        time.sleep(0.1)

# 你的代码：创建 3 个线程，分别传入 "A", "B", "C"
# threads = []
# for name in ["A", "B", "C"]:
#     t = threading.Thread(target=task, args=(name,))
#     ...
# for t in threads:
#     ...
# print("所有线程结束")


# ============================================================
# 练习2：继承 Thread
# ============================================================
# TODO: 定义一个 DownloadThread 继承 threading.Thread
# __init__ 接收 url，run() 里模拟下载
# run() 打印 "开始下载: {url}"，sleep 1秒，打印 "下载完成"

class DownloadThread(threading.Thread):
    def __init__(self, url: str):
        # 你的代码...
        pass

    def run(self):
        # 你的代码...
        pass

# 验证（时间够的话取消注释）
# threads = [
#     DownloadThread("http://a.com/file1"),
#     DownloadThread("http://a.com/file2"),
# ]
# for t in threads: t.start()
# for t in threads: t.join()


# ============================================================
# 练习3：线程池（推荐方式）
# ============================================================
# TODO: 用 ThreadPoolExecutor 并发下载
# urls = ["url1", "url2", "url3", "url4", "url5"]
# 用 executor.map 或 executor.submit

def download(url: str) -> str:
    time.sleep(0.5)
    return f"{url} 下载完成（大小: {len(url) * 100}KB）"

# 你的代码...
# urls = [f"http://example.com/file{i}" for i in range(5)]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     ...


# ============================================================
# 练习4：竞态条件 + Lock
# ============================================================
# TODO: 先运行下面的代码，观察输出是否等于 100000
# 然后加上 Lock 修复

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10000):
        # 你的代码... 用 with lock: 保护 counter += 1
        pass

# 验证
# threads = [threading.Thread(target=increment) for _ in range(10)]
# for t in threads: t.start()
# for t in threads: t.join()
# print(f"counter = {counter}")   # 应该是 100000


# ============================================================
# 练习5：生产者-消费者
# ============================================================
# TODO: 补全生产者-消费者模式

import queue

def producer(q: queue.Queue, items: list):
    """把 items 里的每个元素放入队列，每放一个 sleep 0.2s"""
    # 你的代码...
    pass

def consumer(q: queue.Queue, name: str):
    """从队列取数据，打印 消费者{name} 消费了 {item}"""
    # 你的代码...
    pass

# 验证
# q = queue.Queue()
# items = ["任务1", "任务2", "任务3", "任务4", "任务5"]
# t1 = threading.Thread(target=producer, args=(q, items))
# t2 = threading.Thread(target=consumer, args=(q, "A"))
# t3 = threading.Thread(target=consumer, args=(q, "B"))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# q.put(None)  # 通知消费者结束
# q.put(None)  # 两个消费者需要两个停止信号
# t2.join()
# t3.join()
# print("全部完成")


# ============================================================
# ✅ 完成标记
# ============================================================
print("\n✅ 多线程练习完成！")
