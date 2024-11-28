from django.db import models

class Task(models.Model):
    taskName = models.CharField(max_length=300)
    description = models.TextField()
    PRIORITY = [("N", "None"), ("H", "High"), ("M", "Medium"), ("L", "Low")]
    priority = models.CharField(choices=PRIORITY, default="N", max_length=1)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.taskName
