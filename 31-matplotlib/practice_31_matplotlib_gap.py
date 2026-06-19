"""
31 - Matplotlib 补缺练习：直方图

运行：
    python practice_31_matplotlib_gap.py

如果提示没有 matplotlib：
    pip install matplotlib
"""

from pathlib import Path

import numpy as np


OUTPUT_DIR = Path(__file__).with_name("charts")


def load_matplotlib():
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("当前环境没有安装 matplotlib，请先运行：pip install matplotlib")
        return None

    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False
    return plt


def main() -> None:
    plt = load_matplotlib()
    if plt is None:
        return

    OUTPUT_DIR.mkdir(exist_ok=True)

    # 模拟一批 API 延迟数据
    rng = np.random.default_rng(42)
    latency = rng.normal(180, 80, size=500)
    latency = np.maximum(latency, 10)  # 最低 10ms

    # --- 直方图 ---
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(latency, bins=25, edgecolor="white", color="steelblue")
    ax.set_title("API 延迟分布")
    ax.set_xlabel("延迟 (ms)")
    ax.set_ylabel("请求数量")
    ax.axvline(np.median(latency), color="red", linestyle="--", label=f"中位数={np.median(latency):.0f}ms")
    ax.axvline(np.percentile(latency, 95), color="orange", linestyle="--", label=f"P95={np.percentile(latency, 95):.0f}ms")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "hist_latency.png", dpi=150)
    plt.close(fig)

    # --- 对比：不同 bins ---
    fig, axes = plt.subplots(1, 3, figsize=(12, 3))
    for i, bins in enumerate([5, 20, 50]):
        axes[i].hist(latency, bins=bins, edgecolor="white", color="steelblue")
        axes[i].set_title(f"bins={bins}")
        axes[i].set_xlabel("延迟 (ms)")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "hist_bins_compare.png", dpi=150)
    plt.close(fig)

    print(f"图表已生成到: {OUTPUT_DIR}")
    print("31 Matplotlib 补缺练习完成！")


if __name__ == "__main__":
    main()
