from django.db import models
# Create your models here.

class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=140)
    owner = models.ForeignKey('auth.User', related_name = 'tweets', on_delete = models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.text
