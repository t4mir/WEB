from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default=' ')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


def to_catjson(self):
    return {
        'id': self.id,
        'name': self.name
    }
