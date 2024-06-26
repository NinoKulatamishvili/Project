from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Clothes(models.Model):
    picture=models.CharField(max_length=300)
    name=models.ForeignKey(Category, on_delete=models.SET('Unknown Category'))
    size=models.CharField(max_length=50)
    colour=models.CharField(max_length=50)
    price=models.CharField(max_length=10)     #როცა რიცხვებზეა საუბარი რას ვირჩევ

    def __str__(self):
        return f"{self.name}_{self.price}"
