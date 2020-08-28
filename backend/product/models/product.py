from django.db import models

class Product(models.Model):

    productName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    productImg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    productBusinessName = models.CharField(max_length=50)