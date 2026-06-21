"""
实验 4 测试模块。

运行：python EXAM_PREP/lab_oop_report/test.py
"""

from mysystem import Admin, User


def main() -> None:
    user = User("zhangsan", "123456")
    print("用户名：", user.get_name())
    print("原密码：", user.get_password())

    user.set_password("abcdef")
    print("修改后密码：", user.get_password())

    admin = Admin("admin", "root123", "系统管理")
    admin.show_info()
    admin.set_password("newroot")
    print("管理员密码：", admin.get_password())


if __name__ == "__main__":
    main()

