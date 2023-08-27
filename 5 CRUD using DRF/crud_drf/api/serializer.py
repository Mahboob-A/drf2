
from rest_framework import serializers 

from .models import Student


# We only need to make methods in the serializer for create (POST) and for update (PUT) methods. 
# For GET and DELETE methods, there are no need to implement any methos 

class StudentSerializer(serializers.Serializer): 
        name = serializers.CharField(max_length=50)
        roll = serializers.IntegerField()
        st_class = serializers.CharField(max_length=5)
        address = serializers.CharField(max_length=255)

        # create method for PUT (Create) Operation to create an object in the database 
        def create(self, validated_data): 
                return Student.objects.create(**validated_data)
        
        # update method for PUT (update) Operation in the database 
        def update(self, instance, validated_data): 
                '''
                instance is the old data already stored in the database and validated data is the data that is coming from the view. 
                here, we are extracting the new data from the validated_data using the model fields as keys. If there are any 
                new value in the validated_data, then it is meant to update, to override the old data with the new data. 
                If the key does not have any value, the it is not meant to update, then just pass the old data again. 
                '''
                instance.name = validated_data.get('name', instance.name)
                instance.roll = validated_data.get('roll', instance.roll)
                instance.st_class = validated_data.get('st_class', instance.st_class)
                instance.address = validated_data.get('address', instance.address)
                
                instance.save()
                return instance




