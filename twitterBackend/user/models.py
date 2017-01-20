from django.db import models

# Create your models here.

"""
class UserData(models.Model):
    followerCount = models.IntegerField()
    followingCount = models.IntegerField()
    followers = models.ManyToManyField('auth.User',related_name = 'followTo', blank = True)
    following = models.ManyToManyField('auth.User',related_name = 'followFrom', blank = True)
    owner =  owner = models.ForeignKey('auth.User', related_name = 'tweets', on_delete = models.CASCADE)
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
