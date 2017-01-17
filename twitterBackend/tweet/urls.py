from django.conf.urls import url
from tweet import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^tweets/$',views.TweetList.as_view()),
    url(r'^tweets/(?P<pk>[0-9]+)/$',views.TweetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
