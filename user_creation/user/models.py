from django.db import models

class user_creation(models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    email=models.EmailField( max_length=254)
    password=models.CharField()
    conform_password=models.CharField()
    image=models.ImageField()
    
class user_data(models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    email=models.EmailField( max_length=254)
    password=models.CharField()
    conform_password=models.CharField()
    image=models.ImageField()
    user_type = models.CharField(max_length=20, default='customer')