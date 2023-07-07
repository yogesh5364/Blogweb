from django.db import models

# Create your models here.
class AddUser(models.Model):
    firstname = models.CharField(max_length=100)
    # columnname        DataType
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.email}"
