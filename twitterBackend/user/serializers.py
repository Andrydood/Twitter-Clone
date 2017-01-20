from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializerOut(serializers.ModelSerializer): #Serializer for when data needs for GET purposes

    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializerCreate(serializers.ModelSerializer):    #Serializer for creating an account

    class Meta:
        model = User
        fields = ('username','email','password')
