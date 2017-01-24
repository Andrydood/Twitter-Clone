from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import Profile

class UserSerializerOut(serializers.ModelSerializer): #Serializer for when data needs for GET purposes

    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializerCreate(serializers.ModelSerializer):    #Serializer for creating an account

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #When being created, call create user function
        return user
