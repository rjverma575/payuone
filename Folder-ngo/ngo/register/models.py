from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=10000)