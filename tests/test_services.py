import pytest
from todos.models import Todo
from todos.services import TodoService


@pytest.mark.django_db
class TestTodoServiceCreate:

    def test_create_todo_with_all_fields(self):
        todo = TodoService.create_todo({
            "title": "Test Todo",
            "description": "A test description",
            "is_completed": False,
        })
        assert todo.id is not None
        assert todo.title == "Test Todo"
        assert todo.description == "A test description"
        assert todo.is_completed is False
        assert todo.created_at is not None

    def test_create_todo_without_optional_fields(self):
        todo = TodoService.create_todo({"title": "Minimal Todo"})
        assert todo.title == "Minimal Todo"
        assert todo.description is None
        assert todo.is_completed is False


@pytest.mark.django_db
class TestTodoServiceGetAll:

    def test_get_all_todos_empty(self):
        todos = TodoService.get_all_todos()
        assert len(todos) == 0

    def test_get_all_todos_returns_all(self):
        TodoService.create_todo({"title": "Todo 1"})
        TodoService.create_todo({"title": "Todo 2"})
        TodoService.create_todo({"title": "Todo 3"})
        todos = TodoService.get_all_todos()
        assert len(todos) == 3


@pytest.mark.django_db
class TestTodoServiceGetById:

    def test_get_todo_by_id_success(self):
        created = TodoService.create_todo({"title": "Find Me"})
        found = TodoService.get_todo_by_id(created.id)
        assert found.id == created.id
        assert found.title == "Find Me"

    def test_get_todo_by_id_not_found(self):
        with pytest.raises(Todo.DoesNotExist):
            TodoService.get_todo_by_id(9999)


@pytest.mark.django_db
class TestTodoServiceUpdate:

    def test_update_todo_title(self):
        todo = TodoService.create_todo({"title": "Old Title"})
        updated = TodoService.update_todo(todo.id, {"title": "New Title"})
        assert updated.title == "New Title"

    def test_update_todo_is_completed(self):
        todo = TodoService.create_todo({"title": "Task"})
        updated = TodoService.update_todo(todo.id, {"is_completed": True})
        assert updated.is_completed is True

    def test_update_todo_multiple_fields(self):
        todo = TodoService.create_todo({"title": "Original", "description": "Old desc"})
        updated = TodoService.update_todo(todo.id, {
            "title": "Updated",
            "description": "New desc",
            "is_completed": True,
        })
        assert updated.title == "Updated"
        assert updated.description == "New desc"
        assert updated.is_completed is True

    def test_update_todo_not_found(self):
        with pytest.raises(Todo.DoesNotExist):
            TodoService.update_todo(9999, {"title": "Nope"})


@pytest.mark.django_db
class TestTodoServiceDelete:

    def test_delete_todo_success(self):
        todo = TodoService.create_todo({"title": "Delete Me"})
        result = TodoService.delete_todo(todo.id)
        assert result is True
        assert Todo.objects.filter(id=todo.id).count() == 0

    def test_delete_todo_not_found(self):
        with pytest.raises(Todo.DoesNotExist):
            TodoService.delete_todo(9999)
