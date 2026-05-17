"""
CS50P 补充 — 正则表达式练习

TODO: 完成以下 4 组练习
运行方式: python practice_27_regex.py
"""

import re

# ============================================================
# 练习1: 验证邮箱
# ============================================================

def is_valid_email(email: str) -> bool:
    """用正则判断是否是合法邮箱格式"""
    # TODO: 实现正则匹配
    # 规则: 用户名@域名.后缀
    # 用户名: 字母/数字/._%+-
    # 域名: 字母/数字/.-
    # 后缀: 至少2个字母
    pass


# 测试
assert is_valid_email("david@harvard.edu") == True
assert is_valid_email("david.malan@cs50.harvard.edu") == True
assert is_valid_email("david@") == False
assert is_valid_email("not-an-email") == False
print("练习1 通过!")


# ============================================================
# 练习2: 提取 Twitter/微博 用户名
# ============================================================

def extract_username(url: str) -> str | None:
    """从 URL 中提取用户名"""
    # TODO: 用正则提取 https://twitter.com/用户名
    # 提示: 用 () 捕获组
    pass


# 测试
assert extract_username("https://twitter.com/davidjmalan") == "davidjmalan"
assert extract_username("https://x.com/cs50") == "cs50"
assert extract_username("https://harvard.edu") is None
print("练习2 通过!")


# ============================================================
# 练习3: 查找并替换
# ============================================================

def normalize_phone(phone: str) -> str:
    """把各种格式的电话号码统一为 010-1234-5678"""
    # TODO: 用 re.sub 把分隔符（空格/点/斜杠）统一为 -
    # "010 1234 5678" → "010-1234-5678"
    # "010.1234.5678" → "010-1234-5678"
    pass


# 测试
assert normalize_phone("010 1234 5678") == "010-1234-5678"
assert normalize_phone("010.1234.5678") == "010-1234-5678"
assert normalize_phone("010/1234/5678") == "010-1234-5678"
print("练习3 通过!")


# ============================================================
# 练习4: 解析日志
# ============================================================

def parse_log_line(line: str) -> dict | None:
    """解析一行日志，提取时间戳、级别、消息"""
    # 日志格式: "2024-01-15 14:30:22 [ERROR] Something went wrong"
    # TODO: 用 3 个捕获组提取 date, level, message
    # 提示: r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)"
    pass


# 测试
log = "2024-01-15 14:30:22 [ERROR] Something went wrong"
result = parse_log_line(log)
assert result is not None
assert result["date"] == "2024-01-15 14:30:22"
assert result["level"] == "ERROR"
assert result["message"] == "Something went wrong"
print("练习4 通过!")
