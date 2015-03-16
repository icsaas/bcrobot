from django.db import models

# Create your models here.
class Subscribe(models.Model):
    username=models.CharField(max_length=20)
    channel=models.CharField(max_length=20)
    url=models.CharField(max_length=40)
