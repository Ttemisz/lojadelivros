from django.db import models

from product.models.category import Category


class Product (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True,null=True)
    price = models.DecimalField(max_digits=10000000000, decimal_places=2) 
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category,blank=True)
    
    def __str__(self):
        return self.title