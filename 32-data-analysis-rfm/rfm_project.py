"""
32 - RFM 用户分组综合项目

运行：
    python rfm_project.py
"""

from datetime import date
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
ORDERS_FILE = BASE_DIR / "orders.csv"
RESULT_FILE = BASE_DIR / "rfm_result.csv"
SEGMENT_SUMMARY_FILE = BASE_DIR / "rfm_segment_summary.csv"
CHART_FILE = BASE_DIR / "rfm_segments.png"


def create_sample_orders() -> None:
    orders = pd.DataFrame(
        [
            {"user_id": 1, "order_date": "2026-05-01", "amount": 199},
            {"user_id": 1, "order_date": "2026-05-10", "amount": 299},
            {"user_id": 2, "order_date": "2026-03-15", "amount": 89},
            {"user_id": 2, "order_date": "2026-04-01", "amount": 120},
            {"user_id": 3, "order_date": "2026-05-18", "amount": 999},
            {"user_id": 4, "order_date": "2026-01-20", "amount": 59},
            {"user_id": 5, "order_date": "2026-05-03", "amount": 499},
            {"user_id": 5, "order_date": "2026-05-08", "amount": 699},
            {"user_id": 5, "order_date": "2026-05-17", "amount": 899},
        ]
    )
    orders.to_csv(ORDERS_FILE, index=False, encoding="utf-8-sig")


def segment_user(row: pd.Series) -> str:
    if row["r_score"] == 1 and row["f_score"] == 1 and row["m_score"] == 1:
        return "高价值用户"
    if row["r_score"] == 1 and row["f_score"] == 1:
        return "活跃用户"
    if row["r_score"] == 0 and row["m_score"] == 1:
        return "沉睡高消费用户"
    return "普通用户"


def build_rfm() -> pd.DataFrame:
    df = pd.read_csv(ORDERS_FILE)
    df["order_date"] = pd.to_datetime(df["order_date"])

    analysis_date = pd.Timestamp(date(2026, 5, 19))

    rfm = df.groupby("user_id").agg(
        last_order_date=("order_date", "max"),
        frequency=("order_date", "count"),
        monetary=("amount", "sum"),
    )

    rfm["recency"] = (analysis_date - rfm["last_order_date"]).dt.days

    rfm["r_score"] = (rfm["recency"] <= rfm["recency"].median()).astype(int)
    rfm["f_score"] = (rfm["frequency"] >= rfm["frequency"].median()).astype(int)
    rfm["m_score"] = (rfm["monetary"] >= rfm["monetary"].median()).astype(int)
    rfm["segment"] = rfm.apply(segment_user, axis=1)

    return rfm.reset_index()


def try_plot(rfm: pd.DataFrame) -> None:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("当前环境没有 matplotlib，已跳过画图。可运行：pip install matplotlib")
        return

    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False

    segment_counts = rfm["segment"].value_counts()

    plt.figure(figsize=(8, 4))
    plt.bar(segment_counts.index, segment_counts.values)
    plt.title("RFM 用户分组人数")
    plt.xlabel("用户分组")
    plt.ylabel("人数")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()
    print(f"图表已导出: {CHART_FILE}")


def main() -> None:
    create_sample_orders()
    rfm = build_rfm()

    print("RFM 结果:")
    print(rfm)

    rfm.to_csv(RESULT_FILE, index=False, encoding="utf-8-sig")
    print(f"结果已导出: {RESULT_FILE}")

    segment_summary = rfm.groupby("segment").agg(
        user_count=("user_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
    )
    segment_summary.to_csv(SEGMENT_SUMMARY_FILE, encoding="utf-8-sig")
    print("分组评估:")
    print(segment_summary)
    print(f"分组评估已导出: {SEGMENT_SUMMARY_FILE}")

    try_plot(rfm)
    print("32 RFM 综合项目完成！")


if __name__ == "__main__":
    main()
