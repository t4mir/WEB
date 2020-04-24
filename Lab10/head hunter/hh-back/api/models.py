from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    city = models.CharField(max_length=90)
    address = models.TextField()
    def __set__(self):
        return self.name

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }

class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField(max_length=90)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __set__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }