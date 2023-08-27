from rest_framework import serializers


# This serializer will convert and deconvert complsex data into pythonic data type (for frontend)
# and from pythonic data type into complex data type (for storing in database)
class StudentSerializer(serializers.Serializer): 
        id = serializers.IntegerField()  # to return the id 
        name = serializers.CharField(max_length=100)
        roll = serializers.IntegerField()
        class_name = serializers.CharField(max_length=15)
        city = serializers.CharField(max_length=50)
        