from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="Note: Accepts Markdown")
    slug = models.SlugField()
    author = models.ForeignKey(User)
    published = models.DateTimeField()

    def __str__(self):
        return self.title

