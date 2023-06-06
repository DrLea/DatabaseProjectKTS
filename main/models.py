from django.utils.timezone import now

from django.core.validators import MinValueValidator
from django.db import models


# USER
class User(models.Model):
    nickname = models.CharField(max_length=20, blank=False, unique=True)
    image = models.ImageField(upload_to=".images/")
    age = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.nickname} - {self.age}'
    

class Interest(models.Model):
    interested_in = models.ManyToManyField(User, related_name='interests')
    name = models.CharField(max_length=20, unique=True, blank=False)


# CONTENT
class Content(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='.images/')
    tag = models.TextField(max_length=20, null=True)
    isApproved = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return f'{self.name} - {self.isApproved}'
    

class _Content(models.Model):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)


    def __str__(self) -> str:
        return f'{self.content_id}'
    
    class Meta:
        abstract = True
    

class Event(_Content):
    location = models.URLField()


class Book(_Content):
    source = models.URLField()


class Video(_Content):
    source = models.URLField()


class File(_Content):
    file = models.FileField(upload_to=".files/")


class Podcast(_Content):
    file = models.FileField(upload_to=".files/")


# COMMENT
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.TextField()