from tweet.models import Tweet
from django.contrib.auth.models import User
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Tweet
        fields = ('id', 'created', 'text', 'owner')

class UserSerializer(serializers.ModelSerializer):

    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tweets',)
