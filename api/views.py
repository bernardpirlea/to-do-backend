from django.utils import tree
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import ToDoSerializer, UserSerializer
from .models import ToDo


@api_view(['POST'])
def register(request):
    if 'email' in request.data and request.data['email']:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
        else:
            return Response({'error': 'Username already exists!'})
        return Response({"token": str(token[0])})
    return Response({'error': 'Email field is required!'})


@ api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todo-list/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>/',
        'Delete': '/todo-delete/<str:pk>/',
    }
    return Response(api_urls)


@ api_view(['GET'])
@ permission_classes((IsAuthenticated,))
def todoList(request):
    user = request.user
    todos = ToDo.objects.filter(owner=user)
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)


@ api_view(['POST'])
@ permission_classes((IsAuthenticated,))
def todoCreate(request):

    user = request.user
    todo = ToDo(owner=user)
    serializer = ToDoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@ api_view(['DELETE'])
@ permission_classes((IsAuthenticated,))
def todoDelete(request, pk):
    user = request.user
    todo = ToDo.objects.get(id=pk)
    if todo.owner != user:
        return Response({"reponse": "You don't have the permission to delete the to do"})
    todo.delete()
    return Response("To do has been deleted successfully.")


@ api_view(['POST'])
@ permission_classes((IsAuthenticated,))
def todoUpdate(request, pk):
    user = request.user
    todo = ToDo.objects.get(id=pk)
    if todo.owner != user:
        return Response({"reponse": "You don't have the permission to edit the to do"})
    serializer = ToDoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
