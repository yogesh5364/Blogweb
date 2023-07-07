from django.db import models
from users.models import AddUser
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class AddBlog(models.Model):
    author = models.ForeignKey(to=AddUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    category = models.CharField(max_length=100, default="coding")

 