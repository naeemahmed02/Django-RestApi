from django.urls import path
from . views import getTasks, createTask
urlpatterns = [
    path('tasks', getTasks, name = 'get-Tasks'),
    path('create-task', createTask, name = 'create-task'),
]
