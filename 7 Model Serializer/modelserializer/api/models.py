from django.db import models

# Create your models here.

class Student(models.Model): 
        name = models.CharField(max_length=50)
        roll = models.IntegerField(unique=True, null=False)
        st_class = models.CharField(max_length=5)
        address = models.CharField(max_length=255)
        

class StudentProxy(Student): 
        class Meta: 
                proxy = True 
                ordering = ['-name']