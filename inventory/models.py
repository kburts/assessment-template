from django.db import models


class Customer(models.Model):
    email = models.EmailField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    quantity = models.IntegerField()
