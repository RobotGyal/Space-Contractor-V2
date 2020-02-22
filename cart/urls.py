from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name= 'cart-home'),
    path('add/', views.cart_add, name= 'cart-add'),
    path('cart_display/', views.cart_display, name= 'cart-display')

]