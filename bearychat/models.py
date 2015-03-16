from django.db import models

# Create your models here.
class Subscribe(models.Model):
    username=models.CharField(max_length=30)
    channel=models.CharField(max_length=30)
    url=models.URLField(max_length=100)
