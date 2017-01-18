from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from tweet.models import Tweet
from tweet.serializers import TweetSerializer
from tweet.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TweetList(generics.ListCreateAPIView):  #Generic class based view to create tweets

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) #If user is not the owner, each tweet is read only

    def perform_create(self,serializer):                #When creating tweet
        serializer.save(owner = self.request.user)      #Owner of tweet is set as the user that sent the request


class UserTweets(APIView):                  #View to get tweets from specific user


    def get(self,request,username,format = None):

        try:
            user = User.objects.get(username = username)

        except User.DoesNotExist:
            raise Http404

        tweets = user.tweets.all()
        serialized = TweetSerializer(tweets,many=True)

        return Response(serialized.data)

class UserTweetsDetail(APIView):         #View to get specific tweet from specific user

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) #If user is not the owner, each tweet is read only

    def getTweet(self,username,pk):      #Fetch tweet from database

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise Http404

        try:
            tweet = user.tweets.get(id=pk)
        except Tweet.DoesNotExist:
            raise Http404

        return user.tweets.get(id=pk)   #Return tweet with associated id

    def get(self,request,username,pk,format = None):        #GET tweet

        tweet = self.getTweet(username,pk);
        serialized = TweetSerializer(tweet)

        return Response(serialized.data)


    def delete(self, request, pk, format=None):         #Delete tweet
        tweet = self.getTweet(username,pk);
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeTweet(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def getTweet(self,username,pk):      #Fetch tweet from database

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise Http404

        try:
            tweet = user.tweets.get(id=pk)
        except Tweet.DoesNotExist:
            raise Http404

        return user.tweets.get(id=pk)   #Return tweet with associated id

    def put(self,request,pk,username,format=None):

        tweet = self.getTweet(username,pk)
        tweet.CountLikes(self.request.user)
        return Response(status=status.HTTP_201_CREATED)
