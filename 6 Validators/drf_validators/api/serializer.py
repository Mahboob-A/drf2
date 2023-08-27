
from rest_framework import serializers 

from .models import Student


# We only need to make methods in the serializer for create (POST) and for update (PUT) methods. 
# For GET and DELETE methods, there are no need to implement any methos 


# # Video 6 : Validation in DRF | GS # 
# Custom Validators Methods (these has highest priority, 1st priority)
# the custom method name can be anyting - as our choice 
def name_starts_with_m(value): 
        if value[0].lower() != 'm': 
                raise serializers.ValidationError('Name must begin with M')
        # no need to return the value 

# VIdeo : 6 - Validators In Django Rest Framework  
class StudentSerializer(serializers.Serializer): 
        name = serializers.CharField(max_length=50, validators=[name_starts_with_m])
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

        # Video 6 : Validation in DRF | GS # 
        # FIeld Level Validation (these has 2nd priority if Validator methods are created. Else 1st priority)
        # These validate methods are invoked automatically when the .is_valid() is called. 
        # rule is def validate_fieldname(self, value) (value is naming convention) write validte then the field to validate
        # just like the clean_fieldname in django's form validation 
        def validate_roll(self, value): 
                if value > 250: 
                        raise serializers.ValidationError('Roll Must Be Less Than Or Equal To 250')
                return value 

        # Object Level Validation : (these has 3rd priority if Validators and Field validators are implemented. 
        # if Field validators implemeted, then 2nd proirty - i.e these has least priority.)
        # in Object level validation, we just need to write def validate(self, data) (no field name) 
        # when we want to validate multiple fields. (data is a dict, and naming the variable data is naming convention)
        def validate(self, data): 
                # print(data)
                name = data.get('name')
                st_class = data.get('st_class')
                
                if name.lower() == 'mdemo' or name.lower() == 'test': 
                        raise serializers.ValidationError('Name must not be demo or test')
                if  st_class.lower() == 'xii': 
                        raise serializers.ValidationError('Class must be X or XI')
                return data 


