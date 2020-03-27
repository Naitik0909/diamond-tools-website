from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
