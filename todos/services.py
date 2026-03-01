from .models import Todo


class TodoService:

    @staticmethod
    def get_all_todos():
        return Todo.objects.all()

    @staticmethod
    def get_todo_by_id(todo_id):
        return Todo.objects.get(pk=todo_id)

    @staticmethod
    def create_todo(data):
        return Todo.objects.create(**data)

    @staticmethod
    def update_todo(todo_id, data):
        todo = Todo.objects.get(pk=todo_id)
        for key, value in data.items():
            setattr(todo, key, value)
        todo.save()
        return todo

    @staticmethod
    def delete_todo(todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return True
