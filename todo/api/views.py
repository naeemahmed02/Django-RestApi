from django.shortcuts import render, get_object_or_404
from .models import Task
from .serializers import TaskSerializers
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def getTasks(request):
    if request.method == "GET":
        try:
            tasks = Task.objects.all()
            serializer = TaskSerializers(tasks, many= True)
            return JsonResponse(serializer.data, safe=False, status = 200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return JsonResponse({"error": "Unsuported HTTP request"}, satus = 405)

@csrf_exempt
def createTask(request):
    if request.method == "POST":
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = TaskSerializers(data = python_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg": "Task created successfully!"}, status = 201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return JsonResponse({"error": "Unsuported HTTP request"}, satus = 405)