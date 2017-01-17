from tweet.models import Tweet
from django.contrib.auth.models import User
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'created', 'text')

class UserSerializer(serializers.ModelSerializer):

    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tweets',)
