from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



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


@method_decorator(csrf_exempt, name='dispatch')
def toKorz(req):
    items = Korzina.objects.all()
    itog = 0
    for i in items:
        itog += i.summa
    data = {'items': items, 'itog': itog}
    if req.POST.get('type') == 'params':
        print('i am here')
        city = req.POST.get('city')
        name = req.POST.get('name')
        tel = req.POST.get('tel')
        order = Order.objects.create(address=city,name=name,phone=tel)
        print(city,name,tel)
        home = "http://127.0.0.1:8001/"
        return HttpResponse(home)
    return render(req, 'korzina.html', data)


def delete(req, id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')


@method_decorator(csrf_exempt, name='dispatch')
def korzinaZakaz(req):
    return render(req, 'korzina.html')
