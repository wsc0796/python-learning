"""
29 - 数据分析入门练习

这个文件用普通 .py 模拟 Notebook 的“分步骤观察”。
运行：
    python practice_29_data_analysis_intro.py
"""

from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).with_name("orders_intro.csv")


def step(title: str) -> None:
    print(f"\n--- {title} ---")


def create_data() -> None:
    df = pd.DataFrame(
        [
            {"order_id": 1, "city": "南昌", "amount": 199},
            {"order_id": 2, "city": "杭州", "amount": 299},
            {"order_id": 3, "city": "南昌", "amount": 99},
            {"order_id": 4, "city": "上海", "amount": 399},
        ]
    )
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")


def main() -> None:
    create_data()

    step("1. 读取数据")
    df = pd.read_csv(DATA_FILE)
    print(df)

    step("2. 快速观察")
    print(df.head())
    df.info()

    step("3. 简单统计")
    print("订单总额:", df["amount"].sum())
    print("平均订单金额:", df["amount"].mean())

    step("4. 按城市统计")
    city_summary = df.groupby("city")["amount"].sum()
    print(city_summary)

    print("\n29 数据分析入门练习完成！")


if __name__ == "__main__":
    main()
