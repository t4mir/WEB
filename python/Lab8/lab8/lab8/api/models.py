from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)




    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'description': self.description
        }
