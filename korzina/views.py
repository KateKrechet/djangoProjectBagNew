from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
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
    # относится к f2
    # if req.POST.get('type') == 'params':
    #     print('i am here')
    #     city = req.POST.get('city')
    #     name = req.POST.get('name')
    #     tel = req.POST.get('tel')
    #     order = Order.objects.create(address=city,name=name,phone=tel)
    #     print(city,name,tel)
    #     home = "http://127.0.0.1:8001/"
    #     return HttpResponse(home)
    return render(req, 'korzina.html', data)


def delete(req, id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')


@method_decorator(csrf_exempt, name='dispatch')
def korzinaZakaz(req):
    print('1')
    if req.POST:
        print('2')
        adres = req.POST.get('k1')
        name = req.POST.get('k2')
        tel = req.POST.get('k3')
        print(adres, name, tel)
        items = Korzina.objects.all()
        samzakaz = ''
        for one in items:
            samzakaz += one.tovar.opis + ' ' + str(one.count) + ' ' + str(one.summa) + '\n'
        itog = 0
        for i in items:
            itog += i.summa
        Order.objects.create(address=adres, name=name, phone=tel, total=itog,
                                samzakaz=samzakaz)
        items.delete()
        #
        TOKEN = "5454744752:AAFboSLD_pHqFPUXrG_Fup5TVleSker9CXY"
        chat_id = "1899000306"
        message = samzakaz + adres + ' ' + name + ' ' + tel
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение
        # эта строчка позволяет получить данные ТГ
        # https://api.telegram.org/bot5454744752:AAFboSLD_pHqFPUXrG_Fup5TVleSker9CXY/getUpdates
        #
        return JsonResponse({'mes': 'data success', 'link': '../'})
    return redirect('home')
