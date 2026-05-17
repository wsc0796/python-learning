---
aliases:
  - 13-multithreading
---
# 13 — 多线程基础

> 相关笔记：[文件读写与异常](../03-file-exception/theory_03_file_exception.md) · [os 模块](../22-copy-os/theory_22_copy_os.md)

## 重要前提：GIL

```python
# Python 的线程不能真正并行执行 CPU 密集型任务！
# 因为 GIL（全局解释器锁）同一时刻只允许一个线程执行 Python 字节码。
```

| 场景 | 多线程有用？ | 替代方案 |
|------|------------|---------|
| I/O 密集型（网络请求、文件读写、数据库） | ✅ 有用 | `asyncio` 更好 |
| CPU 密集型（计算、循环） | ❌ 没用 | `multiprocessing` |
| 同时等待多个 API | ✅ 有用 | `ThreadPoolExecutor` |

---

## 1. 创建线程

```python
import threading
import time

def task(name):
    print(f"线程 {name} 开始")
    time.sleep(1)
    print(f"线程 {name} 结束")

# 方式1：直接创建 Thread
t = threading.Thread(target=task, args=("A",))
t.start()        # 启动线程
t.join()         # 等待线程结束

# 方式2：继承 Thread
class MyThread(threading.Thread):
    def run(self):
        print("自定义线程运行中")

t2 = MyThread()
t2.start()
t2.join()
```

---

## 2. 线程池（推荐方式）

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url):
    print(f"请求 {url}")
    time.sleep(1)
    return f"{url} 响应"

# 自动管理线程，不用手动 start/join
with ThreadPoolExecutor(max_workers=3) as executor:
    urls = ["http://a.com", "http://b.com", "http://c.com"]

    # 方式1：submit 返回 Future
    futures = [executor.submit(fetch_url, url) for url in urls]
    for f in futures:
        print(f.result())   # 阻塞直到拿到结果

    # 方式2：map 更简洁
    results = executor.map(fetch_url, urls)
    for r in results:
        print(r)
```

---

## 3. 线程安全问题

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # 不是原子操作！可能丢失更新

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # 不是 1000000！因为竞态条件
```

---

## 4. Lock 解决竞态

```python
lock = threading.Lock()
counter = 0

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:          # 自动 acquire + release
            counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # 1000000 ✅
```

---

## 5. 生产者-消费者模式

```python
import queue
import threading
import time

def producer(q):
    for i in range(5):
        item = f"商品-{i}"
        q.put(item)
        print(f"生产: {item}")
        time.sleep(0.3)

def consumer(q):
    while True:
        item = q.get()
        if item is None:    # 停止信号
            break
        print(f"消费: {item}")
        q.task_done()

q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
t1.join()
q.put(None)  # 通知消费者结束
t2.join()
```

---

## 对比 Java

| Java | Python |
|------|--------|
| `new Thread(() -> {...}).start()` | `threading.Thread(target=fn)` |
| `ExecutorService` | `ThreadPoolExecutor` |
| `synchronized` | `with lock:` |
| `synchronized` 方法 | `with self._lock:` |
| `wait() / notify()` | `Condition.wait() / notify()` |
| `volatile` | 无（GIL 已保证单操作原子性） |
