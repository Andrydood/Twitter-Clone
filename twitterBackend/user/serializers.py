from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializerOut(serializers.ModelSerializer): #Serializer for when data needs for GET purposes

    #tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all()) #Tweets shows every tweet associated with this user

    class Meta:
        model = User
        fields = ('id', 'username')

class UserSerializerIn(serializers.ModelSerializer):    #Serializer for logging in and creating an account

    #tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all()) #Tweets shows every tweet associated with this user

    class Meta:
        model = User
        fields = ('id', 'username','password','email')
