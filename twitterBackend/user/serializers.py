from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializerOut(serializers.ModelSerializer): #Serializer for when data needs for GET purposes

    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializerCreate(serializers.ModelSerializer):    #Serializer for creating an account

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #When being created, call create user function
        return user
