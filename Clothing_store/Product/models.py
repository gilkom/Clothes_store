from django.db import models


class Manufacturer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    def __str__(self):
        return self.name

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
