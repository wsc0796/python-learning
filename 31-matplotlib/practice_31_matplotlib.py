"""
31 - Matplotlib 基础练习

运行：
    python practice_31_matplotlib.py

如果提示没有 matplotlib：
    pip install matplotlib
"""

from pathlib import Path


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

    days = [1, 2, 3, 4, 5, 6, 7]
    visitors = [120, 150, 180, 160, 210, 260, 300]

    plt.figure(figsize=(8, 4))
    plt.plot(days, visitors, marker="o")
    plt.title("一周访问量趋势")
    plt.xlabel("天数")
    plt.ylabel("访问量")
    plt.xticks(days, [f"第{day}天" for day in days])
    plt.grid(True)
    plt.savefig(OUTPUT_DIR / "line_visitors.png", dpi=150, bbox_inches="tight")
    plt.close()

    cities = ["南昌", "杭州", "上海", "广州"]
    sales = [1200, 1800, 1500, 2000]

    plt.figure(figsize=(8, 4))
    plt.bar(cities, sales)
    plt.title("城市销售额对比")
    plt.xlabel("城市")
    plt.ylabel("销售额")
    plt.savefig(OUTPUT_DIR / "bar_sales.png", dpi=150, bbox_inches="tight")
    plt.close()

    hours = [1, 2, 3, 4, 5, 6]
    scores = [55, 60, 70, 78, 88, 92]

    plt.figure(figsize=(8, 4))
    plt.scatter(hours, scores)
    plt.title("学习时长与成绩")
    plt.xlabel("学习时长")
    plt.ylabel("成绩")
    plt.grid(True)
    plt.savefig(OUTPUT_DIR / "scatter_hours_scores.png", dpi=150, bbox_inches="tight")
    plt.close()

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(days, visitors, marker="o")
    axes[0].set_title("访问量趋势")
    axes[0].grid(True)

    axes[1].bar(cities, sales)
    axes[1].set_title("销售额对比")

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dashboard.png", dpi=150, bbox_inches="tight")
    plt.close(fig)

    conversion_rate = [0.08, 0.09, 0.11, 0.1, 0.12, 0.13, 0.15]
    fig, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(days, visitors, marker="o", color="tab:blue", label="访问量")
    ax1.set_xlabel("天数")
    ax1.set_ylabel("访问量", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    ax2 = ax1.twinx()
    ax2.plot(days, conversion_rate, marker="s", color="tab:red", label="转化率")
    ax2.set_ylabel("转化率", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    fig.suptitle("访问量与转化率")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dual_axis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"图表已生成到: {OUTPUT_DIR}")
    print("31 Matplotlib 练习完成！")


if __name__ == "__main__":
    main()
