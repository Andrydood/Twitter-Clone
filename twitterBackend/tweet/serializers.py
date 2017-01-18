from tweet.models import Tweet
from django.contrib.auth.models import User
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source = 'owner.username')        #Make owner username read only

    class Meta:
        model = Tweet
        fields = ('id', 'created', 'text', 'owner')

class UserSerializer(serializers.ModelSerializer):

    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all()) #Tweets shows every tweet associated with this user

    class Meta:
        model = User
        fields = ('id', 'username','tweets')
