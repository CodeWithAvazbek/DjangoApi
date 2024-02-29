from django.db import models


class Course(models.Model):
    money_type = [
        ('USD', 'Dollar'),
        ('RUB', 'Rubil'),
        ('UZS', "So'm"),
    ]
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=3, choices=money_type, default="USD")

    def __str__(self):
        return self.name
    
