from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_display, name= 'cart-display'),
    path('add/', views.cart_add, name= 'cart-add')
]