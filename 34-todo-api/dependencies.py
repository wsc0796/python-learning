from service import TodoService

todo_service = TodoService()

def get_todo_service() -> TodoService:
    return todo_service
