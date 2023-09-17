from django.db import models


# Discarding the manytomany realtionship api now as time is running out.
# making the api_view curd using a single model now. 
class Student(models.Model):
        name = models.CharField(max_length=30)
        roll = models.IntegerField()
        grade = models.CharField(max_length=5)
        
        def __str__(self): 
                return self.name
        
class Course(models.Model): 
        students = models.ManyToManyField(Student, related_name='course')
        name = models.CharField(max_length=30)
        duration = models.CharField(max_length=10)
        first_release = models.DateTimeField(auto_now_add=True)
        last_updated = models.DateTimeField(auto_now=True)
        
        def __str__(self): 
                return self.name 
        
        
# Current model that is being used in the curd api in api_view 
class People(models.Model): 
        name = models.CharField(max_length=30)
        money = models.IntegerField()
        city = models.CharField(max_length=30)
        
        def __str__(self): 
                return self.name