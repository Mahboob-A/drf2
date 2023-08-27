from django.contrib import admin

from .models import Student, StudentProxy

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'roll', 'st_class', 'address']
        
@admin.register(StudentProxy)
class StudentProxyAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'roll', 'st_class', 'address']