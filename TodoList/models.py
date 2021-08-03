from django.db import models

class Todo(models.Model):
    ItemName = models.CharField(max_length=255)
    Description = models.TextField()
    Priority = models.CharField(max_length=255)
    CreatedAtTime = models.DateTimeField(auto_now_add=True, null=True)