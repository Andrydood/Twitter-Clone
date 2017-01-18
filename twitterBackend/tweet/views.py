from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from tweet.models import Tweet
from tweet.serializers import TweetSerializer, UserSerializer
from tweet.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions

class TweetList(generics.ListCreateAPIView):  #Generic class based view to list and create tweets

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) #If user is not the owner, each tweet is read only

    def perform_create(self,serializer):                #When creating tweet
        serializer.save(owner = self.request.user)      #Owner of tweet is set as the user that sent the request


class TweetDetail(generics.RetrieveUpdateDestroyAPIView): #Generic class based view to get, modify and delete specific tweets

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) #If user is not the owner, each tweet is read only


class UserList(generics.ListAPIView): #Generic class based view to list users

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): #Generic class based view to show specific user

    queryset = User.objects.all()
    serializer_class = UserSerializer
