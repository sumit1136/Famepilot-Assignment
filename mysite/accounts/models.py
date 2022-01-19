from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=100,unique=True,primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    DOB = models.DateField()
    phone = models.CharField(max_length=10)
