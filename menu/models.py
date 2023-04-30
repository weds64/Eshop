from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

class Products(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits = 999999, decimal_places=2)
    characteristic = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# add products