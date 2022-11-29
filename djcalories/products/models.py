from django.db import models

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
