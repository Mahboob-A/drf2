
from rest_framework import serializers

from .models import Student, Course, People




# Discarding the manytomany realtionship api now as time is running out.
# making the api_view curd using a single model now. 
class StudentSerializer(serializers.ModelSerializer): 
        class Meta: 
                model = Student
                fields = '__all__'
                
class CourseSerializer(serializers.ModelSerializer): 
        # students = serializers.ManyToManyField(
        #         to=Student,
        #         related_name='courses',
        #         read_only=True
        # )
        class Meta: 
                model = Course
                fields = '__all__'


# serializer for the current working model 
class PeopleSerializer(serializers.ModelSerializer): 
        class Meta: 
                model = People
                fields = '__all__'