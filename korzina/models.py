from django.db import models
import requests
from django.contrib.auth.models import  User


# Create your models here.
class Tovar(models.Model):
    opis = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=50)
    discount = models.FloatField(default=1)

    def __str__(self):
        return self.opis


class Korzina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.tovar.price * self.tovar.discount


class Order(models.Model):
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    total = models.IntegerField(blank=True, null=True)
    samzakaz = models.TextField(blank=True, null=True)

class Izbran(models.Model):
    tovar = models.ForeignKey(Tovar,on_delete=models.CASCADE)