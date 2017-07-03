from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.content
    class Meta:
        get_latest_by = "creation_date"