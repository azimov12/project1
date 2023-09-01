from rest_framework import serializers
from .models import MyModel, MyOffice

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('name', 'phone')

class MyOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOffice
        fields = ('adress', 'email')        