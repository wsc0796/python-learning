"""
29 - NumPy 基础练习

运行：
    python practice_29_numpy.py
"""

import numpy as np


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def main() -> None:
    section("1. 创建数组")
    scores = np.array([59, 60, 80, 95])
    print("scores:", scores)
    print("type:", type(scores))

    section("2. 数组属性")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("matrix:\n", matrix)
    print("shape:", matrix.shape)
    print("ndim:", matrix.ndim)
    print("dtype:", matrix.dtype)
    print("size:", matrix.size)

    section("3. 随机矩阵")
    rng = np.random.default_rng(seed=42)
    random_ints = rng.integers(1, 10, size=(2, 3))
    random_floats = rng.random((2, 3))
    print("随机整数矩阵:\n", random_ints)
    print("随机小数矩阵:\n", random_floats)

    section("4. 类型转换")
    float_arr = np.array([1.2, 2.8, 3.5])
    print("原数组:", float_arr)
    print("转 int:", float_arr.astype(int))

    section("5. 向量化计算")
    prices = np.array([10, 20, 30, 40])
    discounted = prices * 0.8
    print("原价:", prices)
    print("八折:", discounted)

    section("6. 布尔筛选")
    passed = scores[scores >= 60]
    excellent = scores[scores >= 90]
    print("及格:", passed)
    print("优秀:", excellent)

    section("7. 常用函数")
    print("平均分:", scores.mean())
    print("最高分:", scores.max())
    print("最低分:", scores.min())
    print("总分:", scores.sum())
    repeated = np.array([3, 1, 2, 3, 2])
    print("去重:", np.unique(repeated))
    print("排序:", np.sort(repeated))

    section("8. reshape")
    arr = np.arange(1, 7)
    reshaped = arr.reshape(2, 3)
    print("原数组:", arr)
    print("变成 2x3:\n", reshaped)

    section("9. 矩阵运算")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[10, 20], [30, 40]])
    print("a + b:\n", a + b)
    print("a * b 逐元素相乘:\n", a * b)
    print("a @ b 矩阵乘法:\n", a @ b)

    section("10. 小任务：找出高于平均分的学生")
    names = np.array(["张三", "李四", "王五", "赵六"])
    high_score_names = names[scores > scores.mean()]
    print("高于平均分:", high_score_names)

    print("\n29 NumPy 练习完成！")


if __name__ == "__main__":
    main()
