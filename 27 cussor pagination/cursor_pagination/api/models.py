from django.db import models



class Student(models.Model): 
        name = models.CharField(max_length=30)
        grade = models.CharField(max_length=5)
        roll = models.IntegerField()
        city = models.CharField(max_length=30)
        
        def __str__(self): 
                return self.name
        
 
 # creating this table to see the how the relations in db forms  | 280923, Thursday 
        
class Course(models.Model): 
        student = models.ManyToManyField(Student, blank=True,  related_name='course')
        name = models.CharField(max_length=30)
        start_time = models.DateField()
        end_time = models.DateField() 


class Album(models.Model): 
        name = models.CharField(max_length=30)
        singer = models.CharField(max_length=30)
        total_songs = models.IntegerField()
        
class Song(models.Model): 
        album = models.ForeignKey(Album, on_delete=models.CASCADE)
        name = models.CharField(max_length=30)
        duration = models.DecimalField(max_digits=5, decimal_places=2)
        

        
        

        
        
