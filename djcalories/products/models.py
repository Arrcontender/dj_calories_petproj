from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    category = models.CharField(max_length=350)
    name = models.CharField(max_length=350)
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.cat_name


class Calculator(models.Model):
    user = models.ManyToManyField(User, related_name='user_calculation')
    product = models.ManyToManyField(Products)
    weight = models.IntegerField()
    total_proteins = models.DecimalField(max_digits=500, decimal_places=2)
    total_fats = models.DecimalField(max_digits=500, decimal_places=2)
    total_carbohydrates = models.DecimalField(max_digits=500, decimal_places=2)
    total_calories = models.DecimalField(max_digits=500, decimal_places=2)




