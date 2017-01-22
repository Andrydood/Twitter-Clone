"""twitterBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import tweet.views
import user.views

import rest_framework.authtoken.views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^makeTweet/$',tweet.views.TweetList.as_view()), #POST to this address to make tweet

    url(r'^newuser/$',user.views.UserCreate.as_view()), #POST to this address to make new user

    url(r'^user/$',user.views.UserList.as_view()), #GET here for a list of the users
    url(r'^user/(?P<username>[\w]+)/$',user.views.UserDetail.as_view()), #GET here for details of a user
    url(r'^user/(?P<username>[\w]+)/tweets/$',tweet.views.UserTweets.as_view()), #GET here for a user's tweets
    url(r'^user/(?P<username>[\w]+)/tweets/(?P<pk>[0-9]+)/$',tweet.views.UserTweetsDetail.as_view()), #GET here for a user's specific tweet, DELETE if owner
    url(r'^user/(?P<username>[\w]+)/tweets/(?P<pk>[0-9]+)/like/$',tweet.views.LikeTweet.as_view()), #PUT here to like specific tweet

    url(r'^login/', rest_framework.authtoken.views.obtain_auth_token), #GET here to return token

    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')), #Allows login to the api
]
urlpatterns = format_suffix_patterns(urlpatterns)
