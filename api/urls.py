from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('todo-list/', views.todoList, name='todo-list')
]
