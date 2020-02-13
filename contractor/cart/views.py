from django.shortcuts import render

# Create your views here.
def cart_display(request):
    return render(request, 'cart/cart_display.html')



def cart_add(request):
    return render(request, 'cart/cart_add.html')