from django.contrib import admin

# Register your models here.
from .models import People



@admin.register(People)
class PeopleAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'money', 'city']