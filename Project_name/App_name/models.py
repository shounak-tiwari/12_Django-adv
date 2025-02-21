from django.db import models


# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()
    Stock = models.FloatField()
    