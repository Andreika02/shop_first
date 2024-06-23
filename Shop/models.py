from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/Product/')
    price = models.FloatField()
    desc = models.TextField()
    sale = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    is_availble = models.BooleanField(default=True)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
