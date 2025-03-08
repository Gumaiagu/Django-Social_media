from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(default='', max_length=128)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(default='', blank=True)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


    def __str__(self):
        return self.title
