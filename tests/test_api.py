import pytest
from rest_framework.test import APIClient
from todos.models import Todo


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def sample_todo():
    return Todo.objects.create(
        title="Sample Todo",
        description="Sample description",
        is_completed=False,
    )


@pytest.mark.django_db
class TestCreateTodoAPI:

    def test_create_todo_returns_201(self, client):
        payload = {
            "title": "New Todo",
            "description": "Created via API",
            "is_completed": False,
        }
        response = client.post("/api/todos/", payload, format="json")
        assert response.status_code == 201
        assert response.data["title"] == "New Todo"
        assert response.data["description"] == "Created via API"
        assert response.data["is_completed"] is False
        assert "id" in response.data
        assert "created_at" in response.data

    def test_create_todo_without_title_returns_400(self, client):
        response = client.post("/api/todos/", {"description": "No title"}, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestListTodosAPI:

    def test_list_todos_returns_200(self, client):
        response = client.get("/api/todos/")
        assert response.status_code == 200
        assert isinstance(response.data, list)

    def test_list_todos_returns_all(self, client, sample_todo):
        Todo.objects.create(title="Second Todo")
        response = client.get("/api/todos/")
        assert response.status_code == 200
        assert len(response.data) == 2


@pytest.mark.django_db
class TestRetrieveTodoAPI:

    def test_retrieve_todo_returns_200(self, client, sample_todo):
        response = client.get(f"/api/todos/{sample_todo.id}/")
        assert response.status_code == 200
        assert response.data["id"] == sample_todo.id
        assert response.data["title"] == "Sample Todo"

    def test_retrieve_todo_not_found_returns_404(self, client):
        response = client.get("/api/todos/9999/")
        assert response.status_code == 404
        assert response.data["error"] == "Todo not found"


@pytest.mark.django_db
class TestUpdateTodoAPI:

    def test_update_todo_returns_200(self, client, sample_todo):
        payload = {
            "title": "Updated Title",
            "description": "Updated description",
            "is_completed": True,
        }
        response = client.put(f"/api/todos/{sample_todo.id}/", payload, format="json")
        assert response.status_code == 200
        assert response.data["title"] == "Updated Title"
        assert response.data["description"] == "Updated description"
        assert response.data["is_completed"] is True

    def test_update_todo_not_found_returns_404(self, client):
        payload = {"title": "Ghost", "description": "Nope", "is_completed": False}
        response = client.put("/api/todos/9999/", payload, format="json")
        assert response.status_code == 404

    def test_update_todo_invalid_data_returns_400(self, client, sample_todo):
        response = client.put(f"/api/todos/{sample_todo.id}/", {}, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestDeleteTodoAPI:

    def test_delete_todo_returns_204(self, client, sample_todo):
        response = client.delete(f"/api/todos/{sample_todo.id}/")
        assert response.status_code == 204
        assert Todo.objects.filter(id=sample_todo.id).count() == 0

    def test_delete_todo_not_found_returns_404(self, client):
        response = client.delete("/api/todos/9999/")
        assert response.status_code == 404
