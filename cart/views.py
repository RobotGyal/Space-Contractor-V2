from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, CreateView

# Create your views here.
def cart_home(request):
    return render(request, 'cart/cart_display.html')


def cart_add(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('content'):
            item = Item.objects.all()
            item.name = request.POST.get('name')
            item.content = request.POST.get('content')
            item.save()
        return render(request, 'cart/cart_add.html')
    else:
        return render(request, 'cart/cart_add.html')


def cart_display(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, 'cart/cart_display.html', context)