from django.db import models



class Student(models.Model): 
        name = models.CharField(max_length=30)
        grade = models.CharField(max_length=5)
        roll = models.IntegerField()
        city = models.CharField(max_length=30)
        
        def __str__(self): 
                return self.name

        
        
