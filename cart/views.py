from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView

# Create your views here.
def cart_home(request):
    return render(request, 'cart/cart_display.html')


def cart_add(request):
    if request.method == 'POST':
        item = Item()
        item.name = request.POST.get('name')
        item.content = request.POST.get('content')
        item.author = request.user
        item.save()
        return redirect('cart-display')
    else:
        return render(request, 'cart/cart_add.html')


def cart_display(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, 'cart/cart_display.html', context)