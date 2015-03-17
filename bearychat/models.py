from django.db import models

# Create your models here.
class Subscriber(models.Model):
    username=models.CharField(max_length=30)
    channel=models.CharField(max_length=30)
    url=models.URLField(max_length=100)
    token=models.CharField(max_length=100)
    groupname=models.CharField(max_length=30)
    subtype=models.CharField(max_length=30)

