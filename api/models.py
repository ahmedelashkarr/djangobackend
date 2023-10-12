from django.db import models
from datetime import datetime
# Create your models here.

class brand(models.Model):
    brand = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.brand
    
class color(models.Model):
    color = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.color


class size(models.Model):
    size = models.CharField(max_length=500, null=True)


    def __str__(self) -> str:
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    color = models.ManyToManyField(color)
    size = models.ManyToManyField(size)
    brand = models.ManyToManyField(brand  )
    quantity = models.IntegerField()
    image = models.CharField(max_length=500)
    created = models.DateField( default = datetime.now())

    def __str__(self) -> str:
        return self.name