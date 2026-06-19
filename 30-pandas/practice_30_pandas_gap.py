"""
30 - Pandas 补缺练习：value_counts / merge / dt / 列运算 / astype

运行：
    python practice_30_pandas_gap.py
"""

import pandas as pd


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def main() -> None:
    section("1. value_counts 频数统计")
    df = pd.DataFrame({
        "endpoint": ["/users", "/orders", "/users", "/login", "/users", "/orders"],
        "status": [200, 200, 400, 200, 200, 500],
    })
    print("接口频数:")
    print(df["endpoint"].value_counts())
    print("\n状态码占比:")
    print(df["status"].value_counts(normalize=True))

    section("2. merge 关联两张表")
    users = pd.DataFrame({
        "user_id": [1, 2, 3],
        "username": ["Tom", "Alice", "Bob"],
    })
    orders = pd.DataFrame({
        "order_id": [101, 102, 103, 104],
        "user_id": [1, 2, 1, 5],
        "amount": [199, 299, 399, 99],
    })
    print("inner join (交集):")
    print(orders.merge(users, on="user_id", how="inner"))
    print("\nleft join (保留左表全部):")
    print(orders.merge(users, on="user_id", how="left"))

    section("3. 时间字段拆解")
    logs = pd.DataFrame({
        "timestamp": [
            "2026-06-01 08:15:00",
            "2026-06-01 14:30:00",
            "2026-06-02 09:00:00",
            "2026-06-02 22:45:00",
        ],
        "latency_ms": [120, 350, 80, 200],
    })
    logs["timestamp"] = pd.to_datetime(logs["timestamp"])
    logs["hour"] = logs["timestamp"].dt.hour
    logs["date"] = logs["timestamp"].dt.date
    logs["weekday"] = logs["timestamp"].dt.day_name()
    print(logs)

    section("4. 按小时统计延迟")
    hourly = logs.groupby("hour").agg(
        request_count=("latency_ms", "count"),
        avg_latency=("latency_ms", "mean"),
    )
    print(hourly)

    section("5. groupby 结果列运算")
    endpoint_stats = df.groupby("endpoint").agg(
        total=("endpoint", "size"),
        errors=("status", lambda x: (x >= 400).sum()),
    )
    endpoint_stats["error_rate"] = endpoint_stats["errors"] / endpoint_stats["total"]
    print(endpoint_stats)

    section("6. astype 类型转换")
    raw = pd.DataFrame({
        "id": [1.0, 2.0, 3.0],
        "score": ["80", "95", "76"],
    })
    raw["id"] = raw["id"].astype(int)
    raw["score"] = raw["score"].astype(int)
    print(raw)
    print("dtypes:\n", raw.dtypes)

    print("\n30 Pandas 补缺练习完成！")


if __name__ == "__main__":
    main()
