from django.urls import path
from api.views import TaskSerialzier, TaskDetailSerializer

urlpatterns = [
    path('tasks/', TaskSerialzier.as_view()),
    path('tasks/<int:pk>', TaskDetailSerializer.as_view()),
]

