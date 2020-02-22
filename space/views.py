from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return render(request, 'home.html')

def store_display(request):
    return render(request, 'store_display.html')