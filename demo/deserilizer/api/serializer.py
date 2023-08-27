from rest_framework import serializers 
from .models import Student 

class StudentSerializer(serializers.Serializer): 
        name = serializers.CharField(max_length=100)
        roll = serializers.IntegerField()
        city = serializers.CharField(max_length=50)

        
        def create(self, validated_data):
                return Student.objects.create(**validated_data)
        

'''
Using ModelSerializer 
#####################################
By using serializers.ModelSerializer, you're letting Django Rest Framework 
automatically handle fields, validation, and saving. 
The Meta class inside the serializer specifies which model and fields should be used for serialization. 
Using fields = '__all__' includes all fields from the Student model. 
If you only want to include specific fields, you can list them like fields = ['name', 'roll', 'city'].

With this setup, creating, updating, and validating Student instances will be handled 
automatically by the framework, saving you a lot of manual code.


#####################################

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

'''