from django.db import models


# from .signals import create_auth_token  # importing like this will also allow the signal to work, but 
# the class ApiConfig(AppConfig): inside app.py , the ready method should be implemented to allow the signal work. 

'''
        imporing the signal to create a auth token for the newly registered user.  
        
    in app.py, inside - class ApiConfig(AppConfig):, this method should be implemented to attach the signal to the app. 
    # def ready(self): 
    #     import api.signals 
'''
# Create your models here.

class Student(models.Model): 
        name = models.CharField(max_length=30)
        grade = models.CharField(max_length=5)
        roll = models.IntegerField()
        city = models.CharField(max_length=30)
        
        def __str__(self): 
                return self.name

        
        
