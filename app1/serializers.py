from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from app1.models import Person, Job

class  PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class  JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'    
class  MySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()
class  SecondJobSerializar(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name']