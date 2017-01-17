from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from tweet.models import Tweet
from tweet.serializers import TweetSerializer, UserSerializer

from rest_framework import generics


class TweetList(generics.ListCreateAPIView):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
