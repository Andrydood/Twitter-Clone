from tweet.models import Tweet
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source = 'owner.username')        #Make owner username read only

    class Meta:
        model = Tweet
        fields = ('id', 'created', 'text', 'owner','likes','appreciators')
