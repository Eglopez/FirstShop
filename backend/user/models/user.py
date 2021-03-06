from django.db import models

class User(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
