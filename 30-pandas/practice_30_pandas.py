"""
30 - Pandas 基础练习

运行：
    python practice_30_pandas.py
"""

from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).with_name("students.csv")
RESULT_FILE = Path(__file__).with_name("students_result.csv")
EXTRA_FILE = Path(__file__).with_name("students_extra.csv")


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def create_sample_csv() -> None:
    data = pd.DataFrame(
        [
            {"name": "张三", "city": "南昌", "math": 88, "english": 92},
            {"name": "李四", "city": "南昌", "math": 76, "english": 81},
            {"name": "王五", "city": "杭州", "math": 95, "english": 89},
            {"name": "赵六", "city": "杭州", "math": 58, "english": 66},
            {"name": "钱七", "city": "上海", "math": None, "english": 73},
        ]
    )
    data.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    extra = pd.DataFrame(
        [
            {"name": "孙八", "city": "广州", "math": 82, "english": 88},
            {"name": "周九", "city": "广州", "math": 91, "english": 93},
        ]
    )
    extra.to_csv(EXTRA_FILE, index=False, encoding="utf-8-sig")


def main() -> None:
    create_sample_csv()

    section("1. 读取 CSV")
    df = pd.read_csv(DATA_FILE)
    print(df)

    section("2. 查看基本信息")
    print("前 3 行:")
    print(df.head(3))
    print("\n统计:")
    print(df.select_dtypes(include="number").describe())

    section("3. 选择列")
    print(df[["name", "math"]])
    print("\n用 iloc 取前 2 行:")
    print(df.iloc[:2])
    print("\n用 loc 取南昌学生:")
    print(df.loc[df["city"] == "南昌", ["name", "city", "math"]])

    section("4. 处理缺失值")
    print("缺失值统计:")
    print(df.isna().sum())
    df["math"] = df["math"].fillna(0)

    section("5. 新增计算列")
    df["total"] = df["math"] + df["english"]
    df["passed"] = df["total"] >= 120
    df["level"] = df["total"].apply(lambda total: "优秀" if total >= 170 else "普通")
    print(df)

    section("6. 条件筛选")
    passed_students = df[df["passed"]]
    print(passed_students[["name", "total", "passed"]])

    section("7. 排序")
    ranked = df.sort_values("total", ascending=False)
    print(ranked[["name", "total"]])

    section("8. 分组聚合")
    city_summary = df.groupby("city").agg(
        student_count=("name", "count"),
        avg_total=("total", "mean"),
        max_total=("total", "max"),
    )
    print(city_summary)

    section("9. concat 合并数据")
    extra_df = pd.read_csv(EXTRA_FILE)
    base_columns = ["name", "city", "math", "english"]
    combined = pd.concat([df[base_columns], extra_df], ignore_index=True)
    combined["total"] = combined["math"] + combined["english"]
    combined["passed"] = combined["total"] >= 120
    combined["level"] = combined["total"].apply(
        lambda total: "优秀" if total >= 170 else "普通"
    )
    print(combined)

    section("10. 透视表")
    pivot = pd.pivot_table(
        df,
        values="total",
        index="city",
        columns="level",
        aggfunc="count",
        fill_value=0,
    )
    print(pivot)

    section("11. 导出结果")
    ranked.to_csv(RESULT_FILE, index=False, encoding="utf-8-sig")
    print(f"已导出: {RESULT_FILE}")

    print("\n30 Pandas 练习完成！")


if __name__ == "__main__":
    main()
