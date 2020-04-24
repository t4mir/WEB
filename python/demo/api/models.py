from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default=' ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'Product id = {self.id}, name = {self.name}, price = {self.price}'


def to_js(self):
    return {
        'id': self.id,
        'name': self.name
    }


def to_full(self):
    return {
        'id': self.id,
        'name': self.name,
        'price': self.price,
        'description': self.description
    }
