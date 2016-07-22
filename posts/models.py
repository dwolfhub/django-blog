from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User)
    published = models.DateTimeField()

    def __str__(self):
        return self.title
