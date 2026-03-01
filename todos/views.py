from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .services import TodoService


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request):
        todos = TodoService.get_all_todos()
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            todo = TodoService.get_todo_by_id(pk)
            serializer = self.get_serializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = TodoService.create_todo(serializer.validated_data)
        output = self.get_serializer(todo)
        return Response(output.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            todo = TodoService.update_todo(pk, serializer.validated_data)
            output = self.get_serializer(todo)
            return Response(output.data)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            TodoService.delete_todo(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
