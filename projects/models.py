from django.db import models
import random


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(default = 'Empty')
    main_features = models.TextField(default ='Empty')
    duration = models.CharField(max_length=100)
    description = models.TextField(default = 'Empty')
    technology = models.CharField(max_length=200)
    image = models.FilePathField(path='projects/static/img/')
    video_url = models.CharField(max_length=500)
    obstacles = models.TextField(default = 'Empty')
    successes = models.TextField(default = 'Empty')
    learn = models.TextField(default = 'Empty')


    def __str__(self):
        return self.title



class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.email

