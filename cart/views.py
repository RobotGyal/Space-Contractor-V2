from django.shortcuts import render
from .models import Item

# Create your views here.
def cart_home(request):
    return render(request, 'cart/cart_display.html')


def cart_display(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, 'cart/cart_display.html', context)


def cart_add(request):
    return render(request, 'cart/cart_add.html')