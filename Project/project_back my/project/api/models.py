from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __set__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __set__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='This is good games')
    salary = models.FloatField(max_length=90)
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='games')

    def __set__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }


class SortManager(models.Manager):

    def sort_by_id(self, id):
        return self.order_by('-id')

    def sort_by_name(self, title):
        return self.order_by('title')

    # objects = models.Manager()  # The default manager.
    # sorted_objects = SortManager()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.TextField()
