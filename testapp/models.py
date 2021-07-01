from django.db import models

# Create your models here.
class Products(models.Model):
    Productname=models.CharField(max_length=64)
    CostPrice=models.FloatField()
    Country=models.CharField(max_length=64)
    ORD_DATE=models.DateField()
    ORD_DESCRIPTION=models.TextField()
    Discount=models.FloatField()
    Sellingprice=models.FloatField()
