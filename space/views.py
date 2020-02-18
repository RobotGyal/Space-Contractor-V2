from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# test_data =[
#     {
#         'title':'Space Item',
#         'content':"This is the first space item",
#         'author':'aleiaknight'
#     },
#     {
#         'title':'Star Item',
#         'content':"This is the 1st star item",
#         'author':'aleiaknight'
#     }
# ]



def index(request):
    return render(request, 'home.html')

def store_display(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, 'store_display.html', context)