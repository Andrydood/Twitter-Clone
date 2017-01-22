from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from user.serializers import UserSerializerCreate, UserSerializerOut

from rest_framework import generics
from rest_framework import permissions

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(generics.ListAPIView): #Generic class based view to list users
    queryset = User.objects.all()
    serializer_class = UserSerializerOut

class UserDetail(generics.RetrieveAPIView): #Generic class based view to show specific user
    queryset = User.objects.all()
    serializer_class = UserSerializerOut
    lookup_field = 'username'               #Field can be looked up with using the username


class UserCreate(APIView): #Class to create user

    def post(self, request, format=None):
        serializer = UserSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
