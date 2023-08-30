from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=25, default="")
    phone = models.CharField(max_length=25, default="")

class MyOffice(models.Model):
    adress = models.CharField(max_length=32, default="")
    email = models.CharField(max_length=32, default="")    
    