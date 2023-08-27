from django.db import models

# Create your models here.
class Student(models.Model): 
        name = models.CharField(max_length=100)
        roll = models.IntegerField()
        class_name = models.CharField(max_length=15)
        city = models.CharField(max_length=50)