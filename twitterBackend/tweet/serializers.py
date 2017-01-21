from tweet.models import Tweet
from rest_framework import serializers

class TweetReadSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source = 'owner.username')        #Make these fields read only
    likes = serializers.IntegerField(source = 'appreciators.count')
    class Meta:
        model = Tweet
        fields = ('id', 'created', 'text', 'owner','likes','appreciators')

class TweetMakeSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source = 'owner.username')        #Make these fields read only
    class Meta:
        model = Tweet
        fields = ('id','text','owner')
