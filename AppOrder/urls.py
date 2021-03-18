from django.urls import path
from . import views

app_name = 'AppOrder'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name="add"),
    path('remove/<pk>/', views.remove_from_cart, name="remove"),
    path('cart/', views.cart_view, name="cart"),
    path('increase/<pk>/', views.increase_cart, name="increase"),
    path('decrease/<pk>/', views.decrease_cart, name="decrease"),
]   