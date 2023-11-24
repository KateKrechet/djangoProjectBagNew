from django.db import models


# Create your models here.
class Tovar(models.Model):
    opis = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(max_length=50)
    discount = models.FloatField(default=1)


class Korzina(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.tovar.price*self.tovar.discount
