"""
递归函数练习
规则：先看 theory_25_recursion.md，再手敲每个 TODO。
"""


# TODO 1: 递归倒计时
# 定义 count_down(n)
# 要求：
#   n == 0 时，打印 "结束" 并 return
#   否则打印 n，然后调用 count_down(n - 1)
# 测试：count_down(3)


# TODO 2: 递归求 1~n 之和
# 定义 f(n)
# 要求：
#   f(1) 返回 1
#   其他情况返回 n + f(n - 1)
# 测试：f(5) -> 15


# TODO 3: 递归求阶乘
# 定义 factorial(n)
# 要求：
#   factorial(1) 返回 1
#   其他情况返回 n * factorial(n - 1)
# 测试：factorial(5) -> 120


# TODO 4: 给递归函数加输入检查
# 定义 safe_sum(n)
# 要求：
#   如果 n <= 0，返回 0
#   否则递归求 1~n 之和
# 测试：
#   safe_sum(5) -> 15
#   safe_sum(0) -> 0


# TODO 5: 破坏实验
# 故意写一个没有终止条件的递归函数 bad_recursion(n)
# 调用 bad_recursion(3)，观察 RecursionError
# 然后把调用注释掉，避免后续运行一直报错


if __name__ == "__main__":
    # TODO: 完成上面的函数后，在这里逐个调用测试
    pass
