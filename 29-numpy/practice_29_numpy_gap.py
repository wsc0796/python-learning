"""
29 - NumPy 补缺练习：axis / where / 广播 / 分位数

运行：
    python practice_29_numpy_gap.py
"""

import numpy as np


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def main() -> None:
    section("1. axis 沿轴计算")
    scores = np.array([
        [80, 90, 70],
        [60, 75, 85],
        [95, 88, 92],
    ])
    print("成绩表:\n", scores)
    print("shape:", scores.shape)
    print("全部平均:", scores.mean())
    print("每列(每科)平均 axis=0:", scores.mean(axis=0))
    print("每行(每人)平均 axis=1:", scores.mean(axis=1))
    print("每列求和 axis=0:", scores.sum(axis=0))
    print("每行最大值 axis=1:", scores.max(axis=1))

    section("2. np.where 数组版 if-else")
    latency = np.array([120, 350, 80, 500, 200])
    level = np.where(latency >= 300, "slow", "normal")
    print("延迟:", latency)
    print("分级:", level)

    # 嵌套：三层分类
    level3 = np.where(
        latency >= 500, "very_slow",
        np.where(latency >= 200, "slow", "normal")
    )
    print("三层分级:", level3)

    section("3. 广播")
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    bonus = np.array([10, 20, 30])
    print("矩阵:\n", matrix)
    print("加成:", bonus)
    print("矩阵 + 加成:\n", matrix + bonus)

    # 列方向广播
    col_bonus = np.array([[100], [200], [300]])  # shape (3,1)
    print("矩阵 + 列加成:\n", matrix + col_bonus)

    section("4. 中位数和分位数")
    latency2 = np.array([120, 150, 180, 200, 250, 300, 5000])
    print("延迟数据:", latency2)
    print("平均值 (受极端值影响):", latency2.mean())
    print("中位数 (更稳健):", np.median(latency2))
    print("P95:", np.percentile(latency2, 95))
    print("P99:", np.percentile(latency2, 99))

    section("5. 小任务：接口延迟分析")
    api_latency = np.array([80, 95, 120, 200, 310, 450, 800, 150, 180, 220])
    print(f"请求数: {len(api_latency)}")
    print(f"平均延迟: {api_latency.mean():.1f}ms")
    print(f"中位数延迟: {np.median(api_latency):.1f}ms")
    print(f"P95 延迟: {np.percentile(api_latency, 95):.1f}ms")
    slow = api_latency[api_latency >= 300]
    print(f"慢请求(>=300ms): {len(slow)} 个")
    print(f"慢请求占比: {len(slow) / len(api_latency) * 100:.1f}%")

    print("\n29 NumPy 补缺练习完成！")


if __name__ == "__main__":
    main()
