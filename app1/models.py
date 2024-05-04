from django.db import models

# Create your models here.


class Catogory(models.Model):
    name=models.CharField(max_length=100)

class Product(models.Model):
    price = models.CharField(max_length=150)
    and_price = models.CharField(max_length=15)
    discount_price = models.CharField(max_length=15, null=True,blank=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)