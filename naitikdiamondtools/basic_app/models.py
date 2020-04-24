from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    coverimg1 = models.ImageField(upload_to='images/cover/1', blank=True)
    coverimg2 = models.ImageField(upload_to='images/cover/2', blank=True)
    coverimg3 = models.ImageField(upload_to='images/cover/3', blank=True)
    def __str__(self):
        return self.name
