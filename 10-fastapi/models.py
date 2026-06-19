"""
Pydantic 数据模型。

TaskCreate：外部创建任务时传进来的数据。
TaskRead：系统返回给前端/保存到文件的数据。
"""

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(default=3, ge=1, le=5)


class TaskRead(TaskCreate):
    id: int = Field(ge=1)
    completed: bool = False
