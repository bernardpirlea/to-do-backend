from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('register/', views.register, name='api-register'),
    path('login/', auth_views.obtain_auth_token, name='api-login'),
    path('todo-list/', views.todoList, name='todo-list'),
    path('todo-create/', views.todoCreate, name="todo-Create"),
    path('todo-delete/<str:pk>', views.todoDelete, name="todo-Delete"),
    path('todo-update/<str:pk>', views.todoUpdate, name="todo-Update")
]
