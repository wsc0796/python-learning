"""
17-context-iterator-async: 迷你异步爬虫（Mini Project 可选练习）

模拟同时请求多个 URL，对比同步和异步性能
"""

import asyncio
import time


async def fetch_url(url: str) -> str:
    """模拟 HTTP GET 请求"""
    # TODO: 用 asyncio.sleep 模拟网络延迟（1-2秒随机）
    # TODO: 返回 f"<HTML from {url}>"
    pass


async def sync_style(urls: list[str]):
    """同步风格：逐个请求（对比用）"""
    # 提示：不能用 await 来"假装同步"，用 time.sleep 模拟
    pass


async def async_style(urls: list[str]) -> list[str]:
    """异步风格：并发请求（用 gather）"""
    # TODO: 用 asyncio.gather 并发执行
    pass


async def main():
    urls = [
        "https://api.github.com/users/torvalds",
        "https://api.github.com/users/gaearon",
        "https://api.github.com/users/kennethreitz",
        "https://api.github.com/users/mitsuhiko",
        "https://api.github.com/users/yyx990803",
    ]

    print(f"共 {len(urls)} 个 URL\n")

    # 异步并发
    start = time.time()
    results = await async_style(urls)
    elapsed = time.time() - start
    print(f"\n异步并发耗时: {elapsed:.2f}s")
    print(f"结果数量: {len(results)}")


if __name__ == "__main__":
    asyncio.run(main())
