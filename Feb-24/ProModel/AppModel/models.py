from django.db import models

class AddProduct(models.Model):
    name = models.CharField(max_length=50)  
    selling_price = models.FloatField()
    maximum_retail_price = models.FloatField()  
    flavour = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100, blank=True) 