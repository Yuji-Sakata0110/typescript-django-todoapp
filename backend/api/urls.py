from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_Overview, name='api_overview'),
    path('api/todo_list/', views.todoList, name='todo_list'),
    path('api/detail/<str:pk>/', views.todoDetail, name='todo_detail'),
    path('api/create/', views.todoCreate, name='todo_create'),
    path('api/update/<str:pk>/', views.todoUpdate, name='todo_update'),
    path('api/delete/<str:pk>/', views.todoDelete, name='todo_delete'),
]
