from django.db import models

#Add product model 
class AddProduct(models.Model):
    Name = models.CharField(max_length=50)
    selling_price =  models.FloatField()
    maximum_reatil_price = models.FloatField()
    flavour = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    Images = models.ImageField(upload_to='media/')

