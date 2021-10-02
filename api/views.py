from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer
from .models import ToDo

"""
API Overview
"""


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
def todoList(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def todoCreate(request):

    user = request.user
    todo = ToDo(owner=user)

    serializer = ToDoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def todoDelete(request, pk):
    user = request.user
    todo = ToDo.objects.get(id=pk)
    if todo.owner != user:
        return Response({"reponse": "You don't have the permission to delete the to do"})
    todo.delete()
    return Response("To do has been deleted successfully.")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def todoUpdate(request, pk):
    user = request.user
    todo = ToDo.objects.get(id=pk)
    if todo.owner != user:
        return Response({"reponse": "You don't have the permission to edit the to do"})
    serializer = ToDoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
