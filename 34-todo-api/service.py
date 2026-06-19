"""Service layer for Todo API.

你需要实现四个函数，操作一个全局的 in-memory 列表：

- list_todos() -> list[TodoRead]: 返回全部待办
- create_todo(TodoCreate) -> TodoRead: 创建新待办，自动分配 id
- get_todo(int) -> TodoRead | None: 按 id 查找，不存在返回 None
- delete_todo(int) -> bool: 按 id 删除，返回是否删除了某条

Tips:
- 用一个 list[dict] 或 list[TodoRead] 做内存存储
- id 自增：维护一个 _next_id 计数器
- 函数签名里用 TodoCreate / TodoRead 做类型提示
"""

# TODO: 从 models 导入 TodoCreate, TodoRead
# TODO: 从 typing 导入 Optional（或直接用 | None 语法）
from models import TodoCreate, TodoRead


class TodoNotFoundError(Exception):
    def __init__(self, todo_id: int) -> None:
        self.todo_id = todo_id
        super().__init__(f"Todo {todo_id} 不存在")


class TodoService:
      def __init__(self):
          self._todos: list[dict] = []
          self._next_id: int = 1

      def list_todos(self) -> list[TodoRead]:
          return [TodoRead(**todo) for todo in self._todos]

      def create_todo(self, todo_in: TodoCreate) -> TodoRead:
          todo = {"id": self._next_id, "text": todo_in.text, "completed": False}
          self._todos.append(todo)
          self._next_id += 1
          return TodoRead(**todo)

      def get_todo(self, todo_id: int) -> TodoRead:
          for todo in self._todos:
              if todo["id"] == todo_id:
                  return TodoRead(**todo)
          raise TodoNotFoundError(todo_id)

      def delete_todo(self, todo_id: int) -> None:
          for i, todo in enumerate(self._todos):
              if todo["id"] == todo_id:
                  del self._todos[i]
                  return
          raise TodoNotFoundError(todo_id)