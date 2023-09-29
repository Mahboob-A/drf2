from django.contrib import admin

# Register your models here.

from .models import Student, Course, Album, Song

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'grade', 'roll', 'city']
        
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'start_time', 'end_time', 'get_students']
        filter_horizontal = ('student', )
        def get_students(self, obj): 
                return ', '.join([student.name for student in obj.student.all()])
        
        get_students.short_description = 'Students'
        
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'singer', 'total_songs']
@admin.register(Song)
class SongAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'duration', 'get_album_name']
        
        def get_album_name(self, obj): 
                return obj.album.name if obj.album else None 
        
        get_album_name.short_description = 'Album'