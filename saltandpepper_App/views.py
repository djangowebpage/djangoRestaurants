from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.
from .models import Pizza, Burger
from django.views.decorators.csrf  import  csrf_exempt

def index(request):
    request.session.set_expiry(0)


    ctx={'active_link':'index'}
    return render(request,'food/index.html',ctx)
def pizza(request):
    request.session.set_expiry(0)

    pizzas=Pizza.objects.all()
    ctx={'pizza':pizzas,'active_link':'pizza'}
    return render(request,'food/pizza.html',ctx)
def burger(request):
    request.session.set_expiry(0)

    burgers=Burger.objects.all()
    ctx={'burger':burgers,'active_link':'burger'}
    return render(request,'food/burger.html',ctx)





@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.method=='POST':
        request.session['note'] = request.POST.get('note')
        print(request.session['note'])
        request.session['order'] = request.POST.get('orders')
        print(order)
    ctx={'active_link':'order'}
    return render(request,'food/order.html',ctx)

def success(request):
    order=request.session['order']
    ctx={'order':order}
    return render(request,'food/success.html',ctx)