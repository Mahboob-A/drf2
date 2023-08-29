from django.contrib import admin

# Register your models here.
from .models import Student, Course, People



# Discarding the manytomany realtionship api now as time is running out.
# making the api_view curd using a single model now. 

class CourseInline(admin.TabularInline): 
        model = Course.students.through
        extra = 0 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):   
        # inlines = [CourseInline]   # with this, we can directly add the relationship with the course while creating student 
        list_display = ['id', 'name', 'grade']
        
        
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'display_students', 'first_release', 'last_updated']
        
        def display_students(self, obj): 
                return ', '.join([student.name for student in obj.students.all() ])
        
        display_students.short_description = 'Students Enrolled'
        
        
                
# registering the new model for simple crud using api_view 

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'money', 'city']