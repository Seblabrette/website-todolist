from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=150,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=False, blank=False)

class ListItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=False, blank=False)
    description = models.CharField(max_length=300,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=False, null=True)
    completed = models.BooleanField(default=False, null=False, blank=False)
