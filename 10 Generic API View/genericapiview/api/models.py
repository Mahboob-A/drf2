from django.db import models

        

class People(models.Model): 
        name = models.CharField(max_length=30)
        money = models.IntegerField()
        city = models.CharField(max_length=30)
        
        def __str__(self): 
                return self.name