from django.urls import path

from .views import ListTodo, DetailedTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailedTodo.as_view()),
]
