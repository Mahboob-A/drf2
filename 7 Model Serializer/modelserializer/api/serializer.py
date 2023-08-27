
from rest_framework import serializers 

from .models import Student





# VIdeo : 7 - ModelSerializer In Django Rest Framework  
'''
ModelSerializer : A Replece Of Normal Serializer Class : 

# Topics Covered: 

        A. In ModelSerializer 
                a. we do not need to explicitly write any fields and we also get the create(self, validated_data) for post 
                        and update(self, instance, validated_data) for put request inbuilt. 
                b. We need to add a Meta class inside the ModelSerializer class. We have to define which model this Model Serializer class 
                        would use and pass '__all__' or pass a list of fields to fields variable. 
                c. In important note is that, Model Serializer is soemwhat same as the ModelFrom we use in Django to build form. 
        

        B. We can pass arguments to the fields by 
                a. explicitly writing the field before the meta class
                b. we can use predefined variables arguments and pass a list to it with the fields that needs that argumet
                c. we also can use 'extra_kwargs'. This takes an dict of dict, the first dict the field name, and the field name takes 
                        and nested dict, in the nested dict, we pass the arguments to pass to the field as key, and the value as True/False as value.
                        
        C. We can also add validators to the fields. Adding validators to the ModelSerializer class is just the same as we add validators in the 
                normal serializer class. There are no difference between normal serializer class and ModelSerializer in respect of passing / adding 
                validators to the fields. 


'''

def name_starts_with_m(value): 
        if value[0].lower() != 'm': 
                raise serializers.ValidationError('Name must begin with M')
        # no need to return the value 
        
class StudentSerializer(serializers.ModelSerializer):
        # B. Passing Arguments 
        # name = serializers.CharField(read_only=True)

        # C. Custom Validator 
        name = serializers.CharField(validators=[name_starts_with_m])

        class Meta: 
                model = Student
                fields = '__all__'
                # fields = ['id',  'name', 'roll', 'st_class', 'address'] 
                # read_only_fields = ['name', 'st_class']
                # extra_kwargs = {'name' : {'read_only' : True}}
                


        # # C. Adding Validators. 
        def validate_roll(self, value): 
                if value > 250: 
                        raise serializers.ValidationError('Roll Must Be Less Than Or Equal To 250')
                return value 

        def validate(self, data): 
                # print(data)
                name = data.get('name')
                st_class = data.get('st_class')
                
                if name.lower() == 'mdemo' or name.lower() == 'test': 
                        raise serializers.ValidationError('Name must not be mdemo or test')
                if  st_class.lower() == 'xii': 
                        raise serializers.ValidationError('Class must be X or XI')
                return data 


