from django.urls import path
from .views import TaskListView, TaskFormView, TaskDetailView, TaskDeleteView


app_name = 'tasks'


urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('task/create/', TaskFormView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskFormView.as_view(), name='update'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
]
