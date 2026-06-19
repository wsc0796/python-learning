"""Pydantic models for Todo API.

你需要定义三个模型：

- TodoCreate: 创建待办时用的请求体 — text 是必填字段
- TodoUpdate: 部分更新时用的请求体 — text 是选填字段
- TodoRead: 返回给客户端时用的响应体 — 包含 id, text, completed
"""

# TODO: 从 pydantic 导入 BaseModel
# TODO: 从 typing 导入 Optional（如果你需要表达"选填"）
from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    text : str = Field(min_length=1)

class TodoUpdate(BaseModel):
    text : Optional[str] = Field(default=None, min_length=1)
    completed : Optional[bool] = Field(default=None)

class TodoRead(BaseModel):
    id : int = Field(ge=1)
    text : str = Field(min_length=1)
    completed : bool = Field(default=False) 

# TODO: 定义 TodoCreate，要求 text: str 为必填


# TODO: 定义 TodoUpdate，要求 text: Optional[str] 默认 None（选填）


# TODO: 定义 TodoRead，包含 id: int, text: str, completed: bool = False
