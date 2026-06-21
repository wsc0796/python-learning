"""
实验 4：用户类和管理员类。

User:
- name 可以被子类继承和访问。
- __password 是私有属性，子类不能直接访问。

Admin:
- 继承 User。
- 增加 authority 权限属性。
"""


class User:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.__password = password

    def get_name(self) -> str:
        return self.name

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str) -> None:
        self.__password = password


class Admin(User):
    def __init__(self, name: str, password: str, authority: str) -> None:
        super().__init__(name, password)
        self.authority = authority

    def show_info(self) -> None:
        print(f"管理员用户名：{self.name}")
        print(f"权限：{self.authority}")

