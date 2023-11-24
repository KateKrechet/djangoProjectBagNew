from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(req):
    items = Tovar.objects.all()
    data = {'tovari': items}
    return render(req, 'index.html', data)


def buy(req, id):
    item = Tovar.objects.get(id=id)

    if Korzina.objects.filter(tovar_id=id):
        product = Korzina.objects.get(tovar_id=id)
        product.count += 1
        product.summa = product.calcSumma()
        product.save()

    else:
        Korzina.objects.create(count=1, tovar=item, summa=item.price)
    return redirect('home')


def toKorz(req):
    items = Korzina.objects.all()
    itog=0
    for i in items:
        itog +=i.summa
    data = {'items':items,'itog':itog}
    return render(req,'korzina.html',data)

def delete(req,id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')