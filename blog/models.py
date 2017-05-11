from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
      return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

class Poll(models.Model):
    question = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
      return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    answer = models.CharField(max_length=50, blank=True, null=True)
    value = models.IntegerField(default=0)
    def count(self):
        self.value += 1
        self.save()
