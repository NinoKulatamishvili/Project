from django.db import models

# Create your models here.

class Clothes(models.Model):
    picture=models.CharField(max_length=300)
    name=models.CharField(max_length=200)
    size=models.CharField(max_length=50)
    colour=models.CharField(max_length=50)
    price=models.CharField(max_length=10)     #როცა რიცხვებზეა საუბარი რას ვირჩევ

    def __str__(self):
        return f"{self.name}_{self.price}"
