from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=50) #სქესი
    category_name = models.CharField(max_length=150) #რა პროდუქტია
    def __str__(self):
        return self.category

class Gender(models.Model):
     category = models.CharField(max_length=150)
     def __str__(self):
         return self.category

class Products(models.Model):
    picture=models.CharField(max_length=1000)
    category_name = models.CharField(max_length=150) #რა პროდუქტია
    category=models.ForeignKey(Categories, on_delete=models.SET('Unknown Categories')) #სქესი
    gender=models.ManyToManyField(Gender, related_name='products', blank=True)
    price=models.CharField(max_length=10)     #როცა რიცხვებზეა საუბარი რას ვირჩევ
    stock_quantity = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.category_name}_{self.price}"

class User(AbstractUser):
    products=models.ManyToManyField(Products, related_name='users', blank=True)