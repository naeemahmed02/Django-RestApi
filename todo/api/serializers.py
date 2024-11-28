from . models import Task
from rest_framework import serializers


class TaskSerializers(serializers.Serializer):
    taskName = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length = 3000)
    PRIORITY = [("None"), ("H", "High"), ("M", "Medium"), ("L", "Low")]
    priority = serializers.ChoiceField(choices=PRIORITY, default="N")
    done = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def __str__(self):
        return self.taskName
