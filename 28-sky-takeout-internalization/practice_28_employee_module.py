"""
28 - 苍穹外卖员工模块内化练习

要求：
1. 按 TODO 手敲，不复制粘贴。
2. 先跑出报错，再逐个补齐。
3. 至少做一个破坏实验，并把观察写在文件底部。
"""

from hashlib import md5
from typing import Protocol

from pydantic import BaseModel, Field


ENABLE = 1
DISABLE = 0
DEFAULT_PASSWORD = "123456"


class AccountNotFoundError(Exception):
    pass


class PasswordError(Exception):
    pass


class AccountLockedError(Exception):
    pass


class DuplicateUsernameError(Exception):
    pass


class EmployeeLoginDTO(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class EmployeeDTO(BaseModel):
    id: int | None = None
    username: str = Field(min_length=3, max_length=8)
    name: str = Field(min_length=2, max_length=4)
    phone: str = Field(pattern=r"^1\d{10}$")
    sex: str = Field(pattern=r"^[01]$")
    id_number: str = Field(pattern=r"^[1-9][0-9]{16}[0-9xX]$")


class EmployeeRecord(BaseModel):
    id: int = Field(ge=1)
    username: str
    name: str
    password_hash: str
    phone: str
    sex: str
    id_number: str
    status: int = ENABLE


class EmployeeRead(BaseModel):
    id: int
    username: str
    name: str
    phone: str
    sex: str
    id_number: str
    status: int


class EmployeeLoginVO(BaseModel):
    id: int
    user_name: str
    name: str
    token: str


def hash_password(raw_password: str) -> str:
    """TODO 1：用 md5 计算密码摘要，等价于 Java DigestUtils.md5DigestAsHex。"""
    raise NotImplementedError


def create_fake_token(employee_id: int) -> str:
    """第一关先不做真正 JWT，用可读字符串模拟 token。"""
    return f"fake-token-for-employee-{employee_id}"


def to_employee_read(employee: EmployeeRecord) -> EmployeeRead:
    """TODO 2：把内部 EmployeeRecord 转成不含 password_hash 的 EmployeeRead。"""
    raise NotImplementedError


class EmployeeRepository(Protocol):
    def get_by_username(self, username: str) -> EmployeeRecord | None:
        ...

    def get_by_id(self, employee_id: int) -> EmployeeRecord | None:
        ...

    def insert(self, employee: EmployeeRecord) -> EmployeeRecord:
        ...

    def update(self, employee: EmployeeRecord) -> EmployeeRecord:
        ...

    def list_employees(self, name: str | None = None) -> list[EmployeeRecord]:
        ...


class InMemoryEmployeeRepository:
    def __init__(self) -> None:
        self._employees: dict[int, EmployeeRecord] = {}
        self._next_id = 1

    def get_by_username(self, username: str) -> EmployeeRecord | None:
        """TODO 3：按 username 查找员工，找不到返回 None。"""
        raise NotImplementedError

    def get_by_id(self, employee_id: int) -> EmployeeRecord | None:
        """TODO 4：按 id 查找员工。"""
        raise NotImplementedError

    def insert(self, employee: EmployeeRecord) -> EmployeeRecord:
        """TODO 5：保存员工，并维护 next_id。"""
        raise NotImplementedError

    def update(self, employee: EmployeeRecord) -> EmployeeRecord:
        """TODO 6：更新已有员工；如果不存在，可以直接抛 AccountNotFoundError。"""
        raise NotImplementedError

    def list_employees(self, name: str | None = None) -> list[EmployeeRecord]:
        """TODO 7：列出员工；name 不为空时做模糊过滤。"""
        raise NotImplementedError


class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self.repository = repository

    def login(self, login_dto: EmployeeLoginDTO) -> EmployeeLoginVO:
        """
        TODO 8：实现登录四步：
        1. 按 username 查员工
        2. 不存在抛 AccountNotFoundError
        3. 密码 hash 后比较，不一致抛 PasswordError
        4. status == DISABLE 抛 AccountLockedError
        5. 返回 EmployeeLoginVO
        """
        raise NotImplementedError

    def save(self, employee_dto: EmployeeDTO) -> EmployeeRead:
        """
        TODO 9：新增员工：
        1. username 不能重复
        2. 默认密码为 DEFAULT_PASSWORD
        3. status 默认为 ENABLE
        4. 返回 EmployeeRead
        """
        raise NotImplementedError

    def list_employees(self, name: str | None = None) -> list[EmployeeRead]:
        """TODO 10：调用 repository.list_employees，再转成 EmployeeRead 列表。"""
        raise NotImplementedError

    def change_status(self, employee_id: int, status: int) -> EmployeeRead:
        """TODO 11：修改员工状态。"""
        raise NotImplementedError


def seed_admin(repository: InMemoryEmployeeRepository) -> None:
    admin = EmployeeRecord(
        id=1,
        username="admin",
        name="管理员",
        password_hash=hash_password(DEFAULT_PASSWORD),
        phone="13812312312",
        sex="1",
        id_number="110101199001010047",
        status=ENABLE,
    )
    repository.insert(admin)


def demo() -> None:
    repository = InMemoryEmployeeRepository()
    seed_admin(repository)
    service = EmployeeService(repository)

    login_vo = service.login(EmployeeLoginDTO(username="admin", password="123456"))
    print("登录成功：", login_vo.model_dump())

    created = service.save(
        EmployeeDTO(
            username="tom",
            name="小明",
            phone="13912345678",
            sex="1",
            id_number="110101199001010048",
        )
    )
    print("新增员工：", created.model_dump())

    print("员工数量：", len(service.list_employees()))

    locked = service.change_status(created.id, DISABLE)
    print("已禁用：", locked.model_dump())


if __name__ == "__main__":
    demo()


# 破坏实验记录：
# 1. 现象：
# 2. 我的猜测：
# 3. 真实原因：
# 4. 下次怎么定位：
