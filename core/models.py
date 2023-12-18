from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    imgurl = models.URLField()
    video = models.FileField(upload_to='video/')

class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.TextField()

    def save(self,  *args, **kwargs):
        if self.password:

            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Theater(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hallname = models.CharField(max_length=255)
    imgurl = models.URLField()
    price = models.TextField()
    location = models.CharField(max_length=255)
