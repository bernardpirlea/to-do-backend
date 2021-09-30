from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDo

"""
API Overview
"""


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def todoList(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()
    return Response("To do has been deleted successfully.")


@api_view(['POST'])
def todoUpdate(request, pk):
    todo = ToDo.objects.get(id=pk)
    serializer = ToDoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
