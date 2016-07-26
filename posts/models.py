from django.db import models

# Create your models here.

class Post(models.Model):
    """"Post model"""
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # make the model unicode supported
    # in Python 2.7
    # def __unicode__(self):
    #     return self.title

    def __str__(self):  # Python 3
        return self.title




